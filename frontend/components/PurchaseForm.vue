<template>
    <div class="account-contact">
        <div class="form-group" v-if="isFormReady">
            <div class="row">
                <div class="col-12 col-md-6">
                    <base-input
                        label="First name"
                        :class="{ error: $v.form.firstName.$error }"
                        v-model="$v.form.firstName.$model"
                    />
                </div>
                <div class="col-12 col-md-6 mt-30 mt-md-0">
                    <base-input
                        label="Last name"
                        :class="{ error: $v.form.lastName.$error }"
                        v-model="$v.form.lastName.$model"
                    />
                </div>
            </div>
            <div class="row mt-30">
                <div class="col-12">
                    <base-input
                        label="E-mail"
                        :class="{ error: $v.form.email.$error }"
                        :error="!$v.form.email.email ? 'Enter the correct email' : ''"
                        v-model="$v.form.email.$model"
                    />
                </div>
            </div>
        
            <div class="row mt-30">
                <div class="col-12">
                    <base-input
                        label="Phone number"
                        :class="{ error: $v.form.phone.$error }"
                        v-model="$v.form.phone.$model"
                    />
                </div>
            </div>

            <div class="row mt-30 justify-content-center justify-content-lg-end">
                <div class="col-auto pr-2">
                    <button class="btn btn-outline-black" @click="$router.push('/catalog/')">Cancel</button>
                </div>
                <div class="col-auto pr-2">
                    <button
                        class="btn btn-black"
                        @click="
                            $v.$touch();
                            !$v.$error ? $emit('buy', form) : '';
                        "
                    >
                        {{ btnName }}
                    </button>
                </div>
            </div>
            
            
        </div>
    </div>
</template>
<script>
    import BaseInput from '../components/fields/BaseInput.vue';
    import {required, email} from 'vuelidate/lib/validators';

    export default {
        name: 'PurchaseForm',
        components: {BaseInput},
        props: {
            btnName: {
                type: String,
                required: false,
                default: '',
            },
            showCreateOrderFields: {
                type: Boolean,
                default: false,
            },
        },
        data() {
            return {
                form: {
                    firstName: '',
                    lastName: '',
                    email: '',
                    phone: '',
                },
            };
        },
        computed: {
            isFormReady() {
                return this.$v ? true : false;
            },
            user() {
                return this.$store.state.user.user;
            },
        },
        validations() {
            let form = {
                firstName: {
                    required,
                },
                lastName: {
                    required,
                },
                email: {
                    required,
                    email,
                },
                phone: {
                    required,
                },
            }

            return {
                form: form,
            }
        },
        created() {
            if (this.user) {
                this.form.firstName = this.user.firstName;
                this.form.lastName = this.user.lastName;
                this.form.email = this.user.email;

                if (this.user.profile) {
                    this.form.phone = this.user.phone;
                }
            }
        },
    };
</script>
<style lang="less">
    .account-contact {
        .form-title {
            width: fit-content;
            margin: 0 35px 0px auto;

            @media @extraLarge {
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

        .radio-group {
            .label {
                font-family: 'Inter-Regular';
                font-size: 14px;
                text-transform: uppercase;
                color: @grey4;
            }


            &.error {
                border-color: @red;

                .label {
                    color: @red;
                }
            }

            input {
                &:checked + label {
                    font-family: 'Inter-Medium';
                    opacity: 1;
                }
            }

            .radio-label {
                display: flex;
                align-items: center;
                font-size: 14px;
                line-height: 17px;
                text-transform: uppercase;
                color: @black;
                cursor: pointer;
                opacity: 0.3;


                .color-group {
                    width: 20px;
                    height: 20px;

                    .label-color {
                        width: 100%;
                        height: 100%;
                        margin-right: 10px;
                        border-color: @black;


                        .color {
                            top: 0;
                            left: 0;
                            right: 0;
                            bottom: 0;
                            margin: auto;
                            width: 15px;
                            height: 15px;
                        }
                    }

                }

            }
        }

        .form-group {
            max-width: 540px;
            margin: 40px auto 0px;

            .textarea-group {
                textarea {
                    background: none;
                }
            }

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
