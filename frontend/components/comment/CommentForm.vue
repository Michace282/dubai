<template>
    <div class="form-group">
        <div class="title">A new rewiew for Body Merelyn</div>
        <div class="form mt-45">
            <div class="d-lg-flex">
                <div class="rating-group">
                    <div class="label mb-0 mb-sm-3">your rating</div>
                    <div class="d-flex">
                        <a class="rating" href.prevent @click="rating = i" v-for="i in 5" :key="i">
                            <svg
                                width="30"
                                height="30"
                                viewBox="0 0 25 25"
                                fill="none"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path
                                    v-if="i > rating"
                                    d="M24.2341 8.95635L16.7305 7.87774L13.354 1.07765C13.1282 0.611414 12.5672 0.416536 12.1009 0.642383C11.911 0.734392 11.7576 0.887709 11.6657 1.07765L8.2891 7.87774L0.785523 8.95635C0.430147 9.01317 0.138592 9.26819 0.0351839 9.61289C-0.0560166 9.94501 0.03285 10.3007 0.269648 10.5508L5.70972 15.8502L4.44351 23.3069C4.38651 23.6648 4.53058 24.025 4.81872 24.2448C5.10247 24.4607 5.48415 24.4971 5.80353 24.3386L12.5098 20.7744L19.2161 24.3386L19.6382 24.4324C19.8436 24.4498 20.0471 24.382 20.2009 24.2448C20.489 24.025 20.6331 23.6648 20.5761 23.3069L19.3099 15.8502L24.75 10.5508C24.9868 10.3007 25.0757 9.94501 24.9844 9.61289C24.881 9.26828 24.5895 9.01317 24.2341 8.95635ZM17.6216 14.8654C17.4297 15.0836 17.3439 15.3754 17.3872 15.6627L18.4189 21.7593L12.9319 18.8986C12.6648 18.7719 12.3549 18.7719 12.0877 18.8986L6.60072 21.7593L7.63247 15.6627C7.67574 15.3754 7.58993 15.0837 7.39801 14.8654L2.94274 10.5509L9.0863 9.65983C9.38826 9.60678 9.6484 9.41603 9.78978 9.14396L12.5098 3.61008L15.2299 9.14396C15.3712 9.41603 15.6313 9.60678 15.9333 9.65983L22.0769 10.5509L17.6216 14.8654Z"
                                    fill="#E6C643"
                                />
                                <path
                                    v-else
                                    d="M24.2341 8.95635L16.7305 7.87774L13.354 1.07765C13.1282 0.611414 12.5672 0.416536 12.1009 0.642383C11.911 0.734392 11.7576 0.887709 11.6657 1.07765L8.2891 7.87774L0.785523 8.95635C0.430147 9.01317 0.138592 9.26819 0.0351839 9.61289C-0.0560166 9.94501 0.03285 10.3007 0.269648 10.5508L5.70972 15.8502L4.44351 23.3069C4.38651 23.6648 4.53058 24.025 4.81872 24.2448C5.10247 24.4607 5.48415 24.4971 5.80353 24.3386L12.5098 20.7744L19.2161 24.3386L19.6382 24.4324C19.8436 24.4498 20.0471 24.382 20.2009 24.2448C20.489 24.025 20.6331 23.6648 20.5761 23.3069L19.3099 15.8502L24.75 10.5508C24.9868 10.3007 25.0757 9.94501 24.9844 9.61289C24.881 9.26828 24.5895 9.01317 24.2341 8.95635Z"
                                    fill="#E6C643"
                                />
                            </svg>
                        </a>
                    </div>
                </div>
                <div class="d-flex mt-30 mt-lg-0">
                    <div class="sizes">
                        <drop-down v-if="sizes.length > 0" v-model="size" :options="sizes" label="Size" />
                    </div>
                    <div class="colors" v-if="colors.length > 0">
                        <drop-down :options="colors" v-model="color" label="Color" />
                    </div>
                </div>
            </div>
            <div class="textarea-group mt-30">
                <div class="d-flex align-items-center justify-content-between">
                    <label for="review" class="label m-0">review</label>
                    <div class="characters-count">Сharacters entered: {{ message.length }} / 1000</div>
                </div>
                <textarea
                    type="text"
                    id="review"
                    class="w-100"
                    :class="{ error: $v.message.$error }"
                    v-model="$v.message.$model"
                    @input="message.length > 1000 ? (message = message.substring(0, 1000)) : ''"
                    name="review"
                ></textarea>
            </div>
            <div class="photo-group">
                <div class="label">Upload photos</div>
                <div class="photos">
                    <label for="file" class="photo-label"><img src="~/assets/images/icons/camera.svg" alt="camera" /></label>
                    <input
                        type="file"
                        ref="files"
                        id="file"
                        @change="validateFiles"
                        class="photo-input"
                        accept="image/jpeg, image/png"
                        multiple
                    />
                    <div class="image" v-for="(url, index) in imagesUrl" :key="`iamge ${index}`">
                        <a
                            href.prevent
                            class="remove"
                            @click="
                                imagesUrl.splice(index, 1);
                                files.splice(index, 1);
                            "
                            ><img src="~/assets/images/icons/exit.svg" alt="remove"
                        /></a>
                        <img :src="url" alt="url" />
                    </div>
                </div>
            </div>
            <div class="row mt-30">
                <div class="col-6 col-sm-auto"><button class="btn btn-black" @click="createFeedback">send</button></div>
                <div class="col-6 col-sm-auto">
                    <button class="btn btn-outline-black" @click="$emit('hideForm')">Cancel</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import DropDown from '../fields/DropDown.vue';
    import { required } from 'vuelidate/lib/validators';

    export default {
        name: 'CommentForm',
        components: { DropDown },
        props: {
            sizes: {
                type: Array,
                required: false,
                default: () => {
                    return [];
                },
            },
            colors: {
                type: Array,
                required: false,
                default: () => {
                    return [];
                },
            },
            productId: {
                type: String,
                required: true,
                default: '',
            },
        },
        data() {
            return {
                rating: 1,
                message: '',
                size: '',
                color: '',
                files: [],
                imagesUrl: [],
            };
        },
        validations: {
            message: {
                required,
            },
        },
        methods: {
            createFeedback() {
                let v = this;
                v.$v.$touch();
                if (!v.$v.$error) {
                    v.$apollo
                        .mutate({
                            mutation: require('~/graphql/mutations/feedback/feedbackCreate'),
                            variables: {
                                star: v.rating,
                                product: v.productId,
                                size: v.size,
                                color: v.color,
                                text: v.message,
                                images: v.files,
                            },
                        })
                        .then((data) => {
                            if (data && data.data.feedbackCreate.errors.length == 0) {
                                v.$emit('success');
                            } else {
                                v.$emit('error', data.data.feedbackCreate.errors[0].messages[0]);
                            }
                        })
                        .catch(() => {
                            v.$emit('error', 'Couldnt add review');
                        });
                }
            },
            validateFiles() {
                let v = this;
                let reader;
                for (let j = 0; j < v.$refs.files.files.length; j++) {
                    if (v.files.length < 5) {
                        if (v.$refs.files.files[j].type == 'image/png' || v.$refs.files.files[j].type == 'image/jpeg') {
                            let file = v.$refs.files.files[j];
                            reader = new FileReader();
                            reader.readAsDataURL(v.$refs.files.files[j]);
                            if (v.$refs.files.files[j].size > 10000000) {
                                v.$bvToast.toast(`Please enter valid credentials ${v.$refs.files.files[j].name}`, {
                                    title: 'Upload',
                                    variant: 'danger',
                                });
                            } else {
                                v.files.push(file);
                                reader.onload = (e) => {
                                    const img = new Image();
                                    img.src = e.target.result;
                                    img.onload = () => {
                                        v.imagesUrl.push(img.src);
                                    };
                                };
                            }
                        }
                    } else {
                        v.$bvToast.toast('You can upload a maximum of 5 photos', {
                            title: 'Upload',
                            variant: 'danger',
                        });
                        break;
                    }
                }
                v.$refs.files.type = 'text';
                v.$refs.files.type = 'file';
            },
        },
    };
</script>
<style lang="less" scoped>
    .form-group {
        background: rgba(0, 0, 0, 0.05);
        padding: 30px 40px;

        @media @small {
            padding: 30px 20px;
        }

        .title {
            font-family: 'Inter-Light';
            font-size: 18px;
            line-height: 22px;
            text-transform: uppercase;
            color: @black;
        }

        .label {
            margin-bottom: 15px;
            font-size: 14px;
            line-height: 17px;
            text-transform: uppercase;
            color: @grey4;

            @media @medium {
                display: block;
            }
        }

        .rating-group {
            margin-right: 90px;

            @media @small {
                display: flex;
                align-items: center;
                justify-content: space-between;
                margin: 0px;
            }

            .rating {
                margin-right: 5px;
            }
        }

        .sizes {
            margin-right: 90px;

            @media @small {
                margin-right: 45px;
            }
        }

        .colors {
            @media @small {
                width: 100%;
            }

            .dropdown-group {
                min-width: 190px;

                @media @small {
                    width: 100%;
                    min-width: 100%;
                }
            }
        }

        .characters-count {
            font-family: 'Inter-Light';
            font-size: 14px;
            color: @grey4;

            @media @small {
                font-size: 10px;
            }
        }

        .photo-group {
            margin-top: 30px;

            .photo-input {
                display: none;
            }

            .photo-label {
                width: 90px;
                height: 125px;
                display: flex;
                align-items: center;
                justify-self: center;
                justify-content: center;
                background: @white;
                border: 1px solid @black;
                border-radius: 2px;
                cursor: pointer;
                margin: 0px 15px 0px 0px;

                @media @small {
                    width: 59px;
                    height: 82px;
                    margin: 0px 10px 0px 0px;
                }
            }

            .photos {
                display: flex;
                align-items: center;
                flex-wrap: wrap;

                .image {
                    position: relative;
                    width: 90px;
                    height: 125px;
                    border: 1px solid @black;
                    box-sizing: border-box;
                    border-radius: 2px;
                    margin-right: 15px;

                    .remove {
                        width: 10px;
                        position: absolute;
                        right: 7px;
                        top: 0px;
                        cursor: pointer;

                        img {
                            width: 10px;
                            height: 10px;
                        }
                    }

                    img {
                        width: 100%;
                        height: 100%;
                        object-fit: cover;
                    }
                }
            }
        }

        .btn-black {
            padding: 7px 57px;

            @media @small {
                width: 100%;
                padding: 7px 10px;
            }
        }

        .btn-outline-black {
            padding: 8px 51px 9px 51px;
            @media @small {
                width: 100%;
                padding: 8px 10px 9px 10px;
            }
        }
    }
</style>
