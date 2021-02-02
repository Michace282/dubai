<template>
    <div class="container">
        <div class="row caption-group">
            <div class="col-auto head-caption">
                <img src="~/assets/images/icons/truck.svg" />
                Free shipping within UAE
            </div>
            <div class="col-auto head-caption">
                <img src="~/assets/images/icons/present.svg" />
                Get your present!
            </div>
            <div class="col-auto head-caption">
                <img src="~/assets/images/icons/line.svg" />
                Size charts
            </div>
        </div>
        <b-carousel
            id="carousel-1"
            :interval="4000"
            indicators
            class="index-carousel"
            img-width="1024"
            img-height="480"
        >
            <b-carousel-slide>
                <template #img>
                    <img
                        class="d-block img-fluid w-100"
                        width="1024"
                        height="480"
                        src="~/assets/images/carouselPhoto.jpg"
                        alt="image slot"
                    />
                </template>
                <div class="box">
                    <nuxt-link to="" class="carousel-link">Dress Damiana Grey</nuxt-link>
                    <div class="caption">200 AED <img src="~/assets/images/icons/arrow-right.svg" /></div>
                </div>
            </b-carousel-slide>
        </b-carousel>
        <index-page-categories />
        <div class="advantages-group">
            <base-title title="Our advantages" />
            <div class="row mt-45">
                <div class="col-6 col-sm-4 col-lg advantage" v-for="(advantage, index) in advantages" :key="index">
                    <img :src="require(`~/assets/images/icons/${advantage.icon}`)" />
                    <div class="name">
                        {{ advantage.name }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import IndexPageCategories from '../components/IndexPageCategories.vue';
    export default {
        name: 'index',
        components: { IndexPageCategories },
        data() {
            return {
                advantages: [
                    {
                        icon: 'laptop.svg',
                        name: 'Wide range of products',
                    },
                    {
                        icon: 'calendar.svg',
                        name: 'Monthly update of collections',
                    },
                    {
                        icon: 'dimond.svg',
                        name: 'High quality material',
                    },
                    {
                        icon: 'sale.svg',
                        name: 'Affordable price',
                    },
                    {
                        icon: 'crown.svg',
                        name: 'Comfortable & Stylish',
                    },
                    {
                        icon: 'pen.svg',
                        name: 'We can arrange custom orders according to your measurements',
                    },
                ],
            };
        },
        created() {
            this.$store.commit('set_breadcrumbs', null);
        },
    };
</script>
<style lang="less">
    .index-carousel {
    }
</style>
<style lang="less" scoped>
    .advantages-group {
        margin-top: 90px;

        .advantage {
            display: flex;
            flex-direction: column;
            align-items: center;

            &:first-child {
                .name {
                    margin-top: 9px;
                }
            }

            @media @large {
                margin-bottom: 30px;
            }

            .name {
                max-width: 140px;
                margin-top: 15px;
                text-align: center;

                @media @large {
                    line-height: 22px;
                }
            }
        }
    }

    .caption-group {
        width: fit-content;
        margin: 0 auto;
        padding: 15px 0px;

        @media @medium {
            max-width: 235px;
            overflow-x: auto;
            display: flex;
            flex-wrap: nowrap;
        }

        .head-caption {
            display: flex;
            align-items: center;
            font-size: 14px;

            &:last-child {
                margin-right: 22px;
            }

            img {
                margin-right: 15px;
            }
        }
    }
</style>
