<template>
    <div>
        <div class="row">
            <div class="col-auto pr-0">
                <div class="avatar default"></div>
            </div>
            <div class="col">
                <div class="row justify-content-between justify-content-sm-start">
                    <div class="col-auto medium name">{{ user }}</div>
                    <div class="col-auto d-sm-none">
                        <rating-group :size="20" :rating="parseInt(rating.split('A_')[1])" />
                    </div>
                    <div class="col-12 col-sm-auto date grey-light">
                        {{ $moment(publicateDate).format('DD.MM.YYYY HH:SS') }}
                    </div>
                </div>
                <div class="row mt-2 mt-sm-3">
                    <div class="col-auto d-none d-sm-block">
                        <rating-group :size="20" :rating="parseInt(rating.split('A_')[1])" />
                    </div>
                    <div class="col-auto d-flex align-items-end">
                        <div class="grey-light">
                            Size: <span class="medium">{{ size }}</span>
                        </div>
                    </div>
                    <div class="col-auto d-flex align-items-end">
                        <div class="grey-light">
                            Color: <span class="medium text-capitalize">{{ color }}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="text ml-65">
            {{ text }}
        </div>
        <div class="row ml-65 mt-15" v-if="images && images.length > 0">
            <div class="col-auto pl-md-0 pr-0 pr-md-3" v-for="image in images" :key="image.node.id">
                <a :href="image.node.image" target="_blank">
                    <img class="comment-photo" :src="image.node.image" alt="comment" />
                </a>
            </div>
        </div>
    </div>
</template>
<script>
    import RatingGroup from './RatingGroup.vue';
    export default {
        name: 'CommentItem',
        components: { RatingGroup },
        props: {
            user: {
                type: String,
                required: true,
                default: '',
            },
            text: {
                type: String,
                required: true,
                default: '',
            },
            images: {
                type: Array,
                default: () => {
                    return [];
                },
            },
            color: {
                type: String,
                default: '',
            },
            size: {
                type: String,
                default: '',
            },
            rating: {
                type: String,
                required: true,
                default: '',
            },
            publicateDate: {
                type: String,
                required: true,
                default: '',
            },
        },
    };
</script>
<style lang="less" scoped>
    .ml-65 {
        @media (min-width: 767px) {
            margin-left: 65px;
        }
    }

    .grey-light {
        font-family: 'Inter-Light';
        font-size: 14px;
        color: @grey4;

        @media @small {
            font-size: 12px;
        }

        &.date {
            @media @small {
                font-size: 10px;
            }
        }
    }

    .avatar {
        width: 50px;
        height: 50px;
        object-fit: cover;
        border-radius: 50%;

        @media @small {
            width: 60px;
            height: 60px;
        }

        &.default {
            background: @grey5;
        }
    }

    .medium {
        font-family: 'Inter-Medium';
        color: @black;

        &.name {
            line-height: 22px;
            font-size: 18px;

            @media @small {
                font-size: 14px;
            }
        }
    }

    .text {
        font-family: 'Inter-Light';
        font-size: 18px;
        line-height: 22px;
        color: @black;
        margin-top: 15px;

        @media @small {
            font-size: 14px;
        }
    }

    .comment-photo {
        max-width: 160px;

        @media @small {
            max-width: 59px;
        }
    }
</style>
