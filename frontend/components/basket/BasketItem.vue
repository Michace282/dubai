<template>
    <div class="item-group">
        <a href.prevent class="delete"><img src="~/assets/images/icons/exit.svg" /></a>
        <div class="row">
            <div class="col-auto">
                <img class="photo" src="~/assets/images/product-preview.png" />
            </div>
            <div class="col params">
                <div class="bold name">Dress</div>
                <item-param label="Color" linkName="Change color">
                    <template v-slot:activeItem>
                        <div class="color-group">
                            <input type="checkbox" disabled checked id="color" />
                            <label class="label-color mb-0" for="color">
                                <div class="color"></div>
                            </label>
                        </div>
                    </template>
                    <template v-slot:options>
                        <div class="colors">
                            <div class="color-group">
                                <input type="radio" name="colors" id="color" />
                                <label class="label-color mb-0" for="color">
                                    <div class="color"></div>
                                </label>
                            </div>
                            <div class="color-group">
                                <input type="radio" name="colors" id="color2" />
                                <label class="label-color mb-0" for="color2">
                                    <div class="color"></div>
                                </label>
                            </div>
                            <div class="color-group">
                                <input type="radio" name="colors" id="color3" />
                                <label class="label-color mb-0" for="color3">
                                    <div class="color"></div>
                                </label>
                            </div>
                        </div>
                    </template>
                </item-param>
                <item-param label="Size" linkName="Change size">
                    <template v-slot:activeItem>
                        <div class="bold">XS</div>
                    </template>
                    <template v-slot:options>
                        <div class="sizes">
                            <div class="size-box">
                                <input type="radio" name="sizes" id="size3" />
                                <label class="label-size" for="size3">XS</label>
                            </div>
                            <div class="size-box">
                                <input type="radio" name="sizes" id="size2" />
                                <label class="label-size" for="size2">S</label>
                            </div>
                        </div>
                    </template>
                </item-param>
                <div class="count-group">
                    <a href.prevemt class="control" @click="count > 1 ? count-- : ''">-</a>
                    <input type="text" @input="validate" v-model="count" />
                    <a href.prevemt class="control" @click="count++">+</a>
                </div>
                <div class="bold mt-30">590 AED</div>
            </div>
        </div>
    </div>
</template>
<script>
    import ItemParam from './ItemParam.vue';

    export default {
        name: 'BasketItem',
        components: { ItemParam },
        data() {
            return {
                count: 1,
            };
        },
        methods: {
            validate() {
                if (this.count * 1 + 0 != this.count || !this.count) {
                    this.count = 1;
                }
            },
        },
    };
</script>
<style lang="less" scoped>
    .item-group {
        position: relative;
        padding: 15px 30px 15px 15px;
        background: @white;
        margin-bottom: 15px;

        .delete {
            display: flex;
            position: absolute;
            right: 15px;
            top: 15px;
            z-index: 100;
            cursor: pointer;

            img {
                height: 15px;
            }
        }

        .photo {
            width: 160px;
        }

        .params {
            .bold {
                font-family: 'Inter-Medium';
                font-size: 18px;
                color: @black;
                text-transform: uppercase;

                &.name {
                    padding-right: 15px;
                }
            }

            .colors {
                display: flex;
                justify-content: flex-start;
                align-items: center;
                flex-wrap: wrap;

                .color-group {
                    margin: 0px 10px 12px 0px;
                }
            }

            .color-group {
                display: flex;
                align-items: center;

                .label-color {
                    width: 20px;
                    height: 20px;
                }
            }

            .sizes {
                .size-box {
                    margin-right: 10px;

                    .label-size {
                        width: 20px;
                        height: 20px;
                        text-align: center;
                    }
                }
            }

            .label {
                font-family: 'Inter-Light';
                font-size: 18px;
                color: @black;
            }

            .count-group {
                display: flex;
                align-items: center;
                margin-top: 40px;

                .control {
                    cursor: pointer;
                    font-size: 24px;
                    user-select: none;
                }

                input {
                    width: 30px;
                    height: 30px;
                    text-align: center;
                    margin: 0px 5px;
                    border: 1px solid @black;
                    box-sizing: border-box;
                    border-radius: 2px;
                    font-size: 14px;
                    color: @black;
                }
            }
        }
    }
</style>
