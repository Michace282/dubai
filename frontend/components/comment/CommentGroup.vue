<template>
    <ApolloQuery
        :query="require('~/graphql/queries/feedback/feedbackList')"
        :variables="{
            product: id,
            first: 5,
        }"
    >
        <template v-slot="{ result: { error, data }, isLoading, query }">
            <div v-if="isLoading || error" class="loading apollo mt-85"></div>
            <div v-else-if="data && data.feedbackList.edges.length > 0" class="result apollo mt-90">
                <comment-item
                    v-for="(comment, index) in data.feedbackList.edges"
                    :key="index"
                    class="mt-30"
                    user="Anonimus"
                    :text="comment.node.text"
                    :color="comment.node.color.name"
                    :size="comment.node.size.name"
                    :rating="comment.node.star"
                    :publicateDate="comment.node.createdAt"
                />
                <button
                    class="btn btn-outline-black"
                    @click="
                        cursor = data.feedbackList.pageInfo.endCursor;
                        loadMore(query);
                    "
                    v-if="data.feedbackList.pageInfo.hasNextPage"
                >
                    Show more
                </button>
            </div>
        </template>
    </ApolloQuery>
</template>
<script>
    import CommentItem from '../../components/comment/CommentItem.vue';

    export default {
        name: 'CommentGroup',
        components: { CommentItem },
        props: {
            id: {
                type: String,
                required: false,
                default: null,
            },
        },
        data() {
            return {
                cursor: '',
            };
        },
        methods: {
            async loadMore(query) {
                await query.fetchMore({
                    variables: {
                        after: this.cursor,
                    },
                    updateQuery: (prev, { fetchMoreResult }) => {
                        let prevAds = prev.feedbackList.edges;
                        let nextAds = fetchMoreResult.feedbackList.edges;
                        let result = [];
                        if (nextAds.length > 0) {
                            result = [...prevAds, ...nextAds];
                        } else {
                            result = prevAds;
                        }

                        prev.feedbackList.pageInfo = fetchMoreResult.feedbackList.pageInfo;
                        prev.feedbackList.edges = result;

                        return prev;
                    },
                });
            },
        },
    };
</script>
<style lang="less" scoped>
    .btn-outline-black {
        margin: 45px 0px 0px 65px;
        padding: 11px 35px;
    }
</style>
