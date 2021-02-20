<template>
    <ApolloQuery
        :query="require('~/graphql/queries/feedback/feedbackList')"
        :variables="{
            product: id,
            first: 5,
        }"
    >
        <template v-slot="{ result: { error, data }, isLoading, query }">
            <transition name="fade" mode="out-in">
                <div v-if="isLoading || error" class="loading apollo mt-85" key="loader"></div>
                <div v-else-if="data && data.feedbackList.edges.length > 0" class="comment-item-group mt-90" key="comments">
                    <comment-item
                        v-for="(comment, index) in data.feedbackList.edges"
                        :key="index"
                        class="mt-30"
                        :user="`${comment.node.user.firstName} ${comment.node.user.lastName}`"
                        :text="comment.node.text"
                        :color="comment.node.color.name"
                        :size="comment.node.size.name"
                        :rating="comment.node.star"
                        :publicateDate="comment.node.createdAt"
                        :images="comment.node.feedbackimageSet.edges"
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
                <div v-else class="mt-4" key="404">
                    <div>Reviews not found :(</div>
                </div>
            </transition>
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
    .comment-item-group {
        max-width: 790px;
    }

    .btn-outline-black {
        margin: 45px 0px 0px 65px;
        padding: 11px 35px;
    }
</style>
