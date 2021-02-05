<template>
    <div>
        <div class="row">
            <div class="col-auto pr-0">
                <div class="avatar default"></div>
            </div>
            <div class="col">
                <div class="row">
                    <div class="col-auto medium name">{{ user }}</div>
                    <div class="col-auto grey-light">
                        {{ $moment(publicateDate).format('DD.MM.YYYY HH:SS') }}
                    </div>
                </div>
                <div class="row mt-15">
                    <div class="col-auto">
                        <rating-group :size="20" :rating="parseInt(rating.split('STAR')[1])" />
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
        <div class="row ml-65"></div>
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
        margin-left: 65px;
    }

    .grey-light {
        font-family: 'Inter-Light';
        font-size: 14px;
        color: @grey4;
    }

    .avatar {
        width: 50px;
        height: 50px;
        object-fit: cover;
        border-radius: 50%;

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
        }
    }

    .text {
        font-family: 'Inter-Light';
        font-size: 18px;
        line-height: 22px;
        color: @black;
        margin-top: 15px;
    }
</style>
