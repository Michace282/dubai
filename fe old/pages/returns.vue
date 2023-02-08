<template>
    <div class="container">
        <base-title title="Returns & Refunds"/>
        <div class="accordion mt-45" role="tablist">
            <b-card no-body class="mb-1">
                <b-card-header header-tag="header" role="tab">
                    <b-button block v-b-toggle.accordion-1>What is your Returns Policy?</b-button>
                </b-card-header>
                <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
                    <b-card-body>
                        <b-card-text>
                            <p>
                                We understand that sometimes something just doesn't work for you and you want to
                                exchange it or return it and ask for your money back.
                            </p>
                            <p>
                                Don’t worry, as long as the item is still in its original condition (the condition in
                                which it was sold with all tags attached and not worn or damaged) and in the original
                                packaging (including shoe boxes for shoes), we accept returns, subject to a few
                                exceptions and the rules below. None of these rules affect your rights under the
                                applicable Federal Laws of the United Arab Emirates as applied in the Emirate of Dubai.
                            </p>
                            <p>
                                Of course, it's fine to try on an item, like you would in a shop, but please don't
                                actually wear it. Shoes especially must not be tried on any floors which may mark, scuff
                                or damage the sole or any part of the shoe in any way.
                            </p>
                            <p>
                                If an item is returned to us damaged, worn or in an unsuitable condition, we won't be
                                able to give you a refund or exchange and we may have to send it back to you (and ask
                                you to cover the delivery costs). All items are inspected on return.
                            </p>
                            <p><b>Items which unfortunately can not be returned for refund or exchange:</b></p>
                            <p>
                                Hygiene and our customer’s safety are super important to us, so unfortunately, certain
                                items can not be returned for refund or exchange. These mainly include:
                            </p>

                            <p></p>
                            <p>
                                - Face masks <br/>
                                - Beauty or Tanning Products <br/>
                                - Ladies tights
                            </p>
                            <p class="text-uppercase mt-45 mb-0">
                                <b>If you still have any questions, please contact us.</b>
                            </p>
                            <nuxt-link to="/contacts/" class="btn btn-black mt-15">Contact</nuxt-link>
                        </b-card-text>
                    </b-card-body>
                </b-collapse>
            </b-card>
            <b-card no-body class="mb-1">
                <b-card-header header-tag="header" role="tab">
                    <b-button block v-b-toggle.accordion-2
                    >Can I return an item for an exchange instead of a refund?
                    </b-button
                    >
                </b-card-header>
                <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
                    <b-card-body>
                        <b-card-text>
                            <p>
                                Yes - our customers are very important for us so we are happy to offer you an exchange.
                            </p>
                            <p>
                                If you wish to exchange something for the same item in a different size or colour and,
                                provided we have your chosen size or colour in stock, we shall aim to send the
                                replacement item back to you as soon we receive the original from you.
                            </p>
                            <p>
                                If we don’t have the correct size or colour available we can order it for you, but this
                                may take a few weeks to arrive. Alternatively, you can place an order for a different
                                item and we shall refund the difference in cost or you can request a full refund.
                            </p>
                            <p class="text-uppercase mt-45 mb-0">
                                <b>If you still have any questions, please contact us.</b>
                            </p>
                            <nuxt-link to="/contacts/" class="btn btn-black mt-15">Contact</nuxt-link>
                        </b-card-text>
                    </b-card-body>
                </b-collapse>
            </b-card>

            <b-card no-body class="mb-1">
                <b-card-header header-tag="header" role="tab">
                    <b-button block v-b-toggle.accordion-3
                    >How do I return something to you for exchange or refund?
                    </b-button
                    >
                </b-card-header>
                <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
                    <b-card-body>
                        <b-card-text>
                            <p>
                                Procedure for Returns – you can return items quickly and easily by following these
                                simple steps:
                            </p>
                            <div class="d-flex">
                                <div class="caption">Step One:</div>
                                <div>
                                    <p>
                                        Contact us as soon as possible through the email or numbers shown below to let
                                        us know that you wish to return an item.
                                    </p>
                                    <p><b class="mr-2">Email:</b> dcs.dancewear@gmail.com</p>
                                    <div class="d-flex mr-2">
                                        <div class="mr-3"><b>Phone:</b></div>
                                        <div>
                                            +971 58 596 7208 <br/>
                                            +971 50 655 3470
                                        </div>
                                    </div>
                                    <p class="mt-15">
                                        We shall be happy to answer any queries and guide you through the steps if
                                        needed.
                                    </p>
                                </div>
                            </div>
                            <div class="d-flex mt-15">
                                <div class="caption">Step Two:</div>
                                <div>We shall send you a link to print a Returns Form and Label.</div>
                            </div>
                            <div class="d-flex mt-15">
                                <div class="caption">Step Three:</div>
                                <div>
                                    Complete the Returns Form and enclose it with the returned item – this helps us to
                                    easily identify who has sent it back to us and what you would like to do.
                                </div>
                            </div>
                            <div class="d-flex mt-15">
                                <div class="caption">Step Four:</div>
                                <div>Stick the Returns Label to the outside of the parcel.</div>
                            </div>
                            <div class="d-flex mt-15">
                                <div class="caption">Step Five:</div>
                                <div>
                                    <p>
                                        Contact the courier company on the number shown on the Returns Form to arrange a
                                        comfortable time for them to collect the item from you to return it to us.
                                    </p>
                                    <p>
                                        Please note that we shall need you to pay the delivery cost of returning any
                                        items by courier. Alternatively, you may be able to return the item in person by
                                        arrangement with one of our representatives.
                                    </p>
                                    <p>
                                        Items must be returned to us no later than 14 working days from the day the item
                                        was received by you.
                                    </p>
                                </div>
                            </div>
                            <p class="mt-15">
                                Provided the item is returned in its original condition and packaging (as set out
                                above), we aim to send the replacement item requested (if available) or refund you by
                                way of the original payment method, within a maximum of 14 working days of receiving the
                                returned or/and exchanged item.
                            </p>
                            <p class="text-uppercase mt-45 mb-0">
                                <b>If you still have any questions, please contact us.</b>
                            </p>
                            <nuxt-link to="/contacts/" class="btn btn-black mt-15">Contact</nuxt-link>
                        </b-card-text>
                    </b-card-body>
                </b-collapse>
            </b-card>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'returns',
        head() {
            return {
                title: 'Returns',
                meta: [
                    {
                        hid: 'description',
                        name: 'description',
                        content: 'Returns',
                    },
                ],
            };
        },
        created() {
            this.$store.commit('set_breadcrumbs', [
                {route: '/', name: 'Home'},
                {route: {name: 'payment'}, name: 'payment & delivery'},
            ]);
        },
    };
</script>
<style lang="less">
.accordion {
    .card {
        border: 0px;

        &:nth-child(even) {
            .card-body {
                background: @white;
            }

            .btn-block {
                background: @white;

                &:focus {
                    background: @white;
                    color: @black;
                }
            }
        }

        .card-header {
            border: 0px;
            padding: 0px;
        }

        .card-body {
            padding: 0px 30px 30px 30px;
            font-family: 'Inter-Light';
            font-size: 18px;
            background: @grey3;

            .caption {
                max-width: 100px;
                width: 100%;
                text-align: right;
                font-weight: 600;
                margin-right: 15px;
            }

            .btn-black {
                padding: 8px 45px;
            }
        }

        .btn-block {
            position: relative;
            padding: 24px 30px;
            border: 0px;
            font-family: 'Inter-Light';
            font-size: 18px;
            text-transform: uppercase;
            color: @black;
            text-align: left;
            background: @grey3;
            font-weight: 600;

            &:after {
                content: url('../assets/images/icons/arrow-collapse.svg');
                position: absolute;
                right: 30px;
                transition: all 0.5s;
            }

            &.collapsed {
                font-weight: normal;

                &:after {
                    transform: rotate(180deg);
                }
            }

            &:focus,
            &:active {
                background: @grey3;
                color: @black;
                box-shadow: unset;
            }
        }
    }
}
</style>
