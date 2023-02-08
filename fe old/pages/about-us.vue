<template>
    <div class="container">
        <!-- <base-title title="Dance Clothes & Shoes Company" class="mt-30"/> -->
        <div class="block-title mt-30">
            <div class="title-shadow">Dance Clothes & Shoes Company</div>
            <h1 class="front-title">Dance Clothes & Shoes Company</h1>
        </div>
        <div class="text-box">
            <div class="text mr-60">
                <p>
                    “DC&S Company” was founded in 2020 and based in Dubai. Our mission – to bring the freshest clothing,
                    shoes and accessories for all the dance community in the UAE!
                </p>
                <p>
                    Our team is Kathryn, Oleg and Kateryna. We are professional dancers, competitors and passionate
                    about dance!
                </p>
                <p>
                    Kathryn started social and ballroom dancing in Dubai 3 years ago and is now a competitive Pro-Am
                    student in Latin and Standard programs, so she understands the needs of students who are just at the
                    beginning of their dance journey up to those who are experienced pro-am competitors.
                </p>
                <img class="d-block d-lg-none mt-45 w-100" src="~/assets/images/about-us-photo.jpg" alt="about us"/>
                <p class="mt-40">
                    Oleg and Kateryna have been professional dancers for 17 years and continued their professional
                    career as dance instructors in Dubai training students in Latin, Ballroom and social dances such as
                    Salsa, Bachata and Argentine Tango. They know how difficult it is for dance instructors, students
                    and lovers of any style of dance to find dance wear which have the right balance of style, comfort,
                    quality, diversity and affordability in the UAE.
                </p>
                <p>
                    We have launched our dance shop to deliver high-quality and stylish dance clothes which will be
                    comfortable to wear for training and performing in any dance style and at any level or which can be
                    worn even for parties!
                </p>
            </div>
            <div class="photo d-none d-lg-block">
                <img src="~/assets/images/about-us-photo.jpg" alt="about us"/>
            </div>
        </div>
        <div class="text-box">
            <div class="photo">
                <img src="~/assets/images/logo-big.png" alt="logo"/>
            </div>
            <div class="text">
                <p>
                    We have a wide range of styles and products which will satisfy any dancer and which we are happy to
                    deliver to you wherever you are based in the UAE in 1-2 days. Don’t worry - if you need to return or
                    exchange anything, we can arrange this for you quickly and easily – just follow the section “Contact
                    Us” in the webpage.
                </p>
                <base-title title="Be Unique – be DC&S!" class="mt-30"/>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'about-us',
        head() {
            return {
                title: 'Dance shop Dubai UAE. Dance company Dubai| DC&S Dubai',
                meta: [
                    {
                        hid: 'description',
                        name: 'description',
                        content: 'Dance Clothes & Shoes Company was founded in 2020 and based in Dubai Our mission – to bring the freshest clothing, shoes and accessories for all the dance community in the UAE!',
                    },
                    {
                        hid: 'keywords',
                        name: 'keywords',
                        content: 'Dance shop Dubai. Dance company Dubai.',
                    },
                ],
            };
        },
        created() {
            this.$store.commit('set_breadcrumbs', [
                {route: '/', name: 'Home'},
                {route: {name: 'about-us'}, name: 'About Us'},
            ]);
        },
    };
</script>
<style lang="less">
    .text {
        .block-title {
            font-family: 'Inter-Medium';
            text-align: center;
            line-height: 77px;

            @media @large {
                max-width: 335px;

                margin: 0 auto;
                line-height: 50px;
            }

            .front-title {
                bottom: unset;
                top: 30px;
                left: 0;
                right: 0;
                margin: auto;

                @media @large {
                    top: 24px;
                }
            }
        }
    }
</style>
<style lang="less" scoped>
    .block-title {
        position: relative;
        font-size: 51px;
        color: @grey3;
        text-transform: uppercase;

        @media @large {
            font-size: 42px;
        }
        @media @medium {
            margin-top: 65px;
        }

        .title-shadow {
            @media @medium {
                display: none;
            }  
        }
        .front-title {
            position: absolute;
            font-family: 'Inter-Medium';
            color: @black;
            left: 0;
            font-size: 36px;
            left: 30px;
            bottom: -2px;

            @media @large {
                font-size: 38px;
                left: 19px;
                bottom: 0px;
            }
            @media @medium {
                font-size: 29px;
                left: 0;
                // bottom: 5px;
            } 
            @media @small {
                font-size: 25px;
            }

        }
    }
    .text-box {
        display: flex;
        justify-content: space-between;
        margin-top: 60px;

        @media @large {
            width: fit-content;
            flex-direction: column;
            justify-content: flex-start;
            margin-top: 45px;
        }

        .text {
            max-width: 530px;
            font-family: 'Inter-Light';
            font-size: 18px;
            color: @black;

            @media @medium {
                line-height: 22px;
            }

            &.mr-60 {
                @media (min-width: 992px) {
                    margin-right: 60px;
                }
            }
        }

        .photo {
            @media @large {
                width: fit-content;
                margin: 0px auto 45px;
            }

            img {
                @media (max-width: 450px) {
                    width: 240px;
                }

                @media (min-width: 992px) {
                    width: 100%;
                }
            }
        }
    }
</style>
