<template>
    <div class="account-contact">
        <base-title class="form-title" title="Contact information" />
        <slot></slot>
        <div class="form-group">
            <div class="row">
                <div class="col-12 col-md-6">
                    <base-input label="first name" />
                </div>
                <div class="col-12 col-md-6 mt-30 mt-md-0">
                    <base-input label="last name" />
                </div>
            </div>
            <div class="row mt-30">
                <div class="col-12">
                    <base-input label="E-mail" />
                </div>
            </div>
            <div class="row mt-30">
                <div class="col-12">
                    <base-input label="address" />
                </div>
            </div>
            <div class="row">
                <div class="col-12 col-md-6 mt-30">
                    <base-input label="postal code" />
                </div>
                <div class="col-12 col-md-6 mt-30">
                    <base-input label="City" />
                </div>
            </div>
            <div class="row mt-30">
                <div class="col-12">
                    <base-input label="Country" />
                </div>
            </div>
            <div class="row mt-30">
                <div class="col-12">
                    <base-input label="Phone number" />
                </div>
            </div>
            <div class="row mt-30 justify-content-center justify-content-lg-end">
                <div class="col-auto pr-2">
                    <button class="btn btn-outline-black" @click="$router.go(-2)">Cancel</button>
                </div>
                <div class="col-auto pr-2">
                    <button class="btn btn-black" @click="$emit('buy')">{{ btnName }}</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import BaseInput from '../components/fields/BaseInput.vue';

    export default {
        name: 'ContactForm',
        components: { BaseInput },
        props: {
            btnName: {
                type: String,
                required: false,
                default: '',
            },
        },
    };
</script>
<style lang="less">
    .account-contact {
        .form-title {
            width: fit-content;
            margin: 0 35px 0px auto;

            @media (max-width: 1199px) {
                margin: 0 -50px 0px auto;
            }

            @media @large {
                line-height: 44px;
                margin: unset;
            }

            .front-title {
                @media @large {
                    max-width: 170px;
                    line-height: 29px;
                    bottom: 10px;
                }
            }
        }

        .form-group {
            max-width: 540px;
            margin: 40px auto 0px;

            @media @large {
                margin: 40px 0px 0px 0px;
            }

            .btn-black {
                padding: 7px 59px;

                @media (max-width: 366px) {
                    margin-top: 10px;
                }
            }

            .btn-outline-black {
                padding: 8px 51px;
            }

            .input-box {
                input {
                    background: @white;
                }
            }
        }
    }
</style>
