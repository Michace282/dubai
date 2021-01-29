<template>
    <div class="item-group">
        <a href.prevent class="delete"><img src="~/assets/images/icons/exit.svg" /></a>
        <div class="row">
            <div class="col-auto">
                <img class="photo" src="~/assets/images/product-preview.png" />
            </div>
            <div class="col params">
                <div class="bold name">Dress</div>
                <div class="row mt-15 align-items-center">
                    <div class="col-auto pr-0">
                        <div class="label">Color</div>
                    </div>
                    <div class="col-auto color-group">
                        <input type="checkbox" disabled id="color" />
                        <label class="label-color mb-0" for="color">
                            <div class="color"></div>
                        </label>
                    </div>
                    <div class="col-auto pr-0">
                        <a href.prevent class="link-grey">Change color</a>
                    </div>
                </div>
                <div class="row mt-15 align-items-center">
                    <div class="col-auto pr-0">
                        <div class="label">Size</div>
                    </div>
                    <div class="col-auto color-box">
                        <div class="bold">XS</div>
                    </div>
                    <div class="col-auto pr-0">
                        <a href.prevent class="link-grey">Change size</a>
                    </div>
                </div>
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
    export default {
        name: 'BasketItem',
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

            .color-group {
                display: flex;
                align-items: center;

                .label-color {
                    width: 20px;
                    height: 20px;
                    border-color: @black;
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
