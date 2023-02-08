<template>
    <div class="item-group">
        <a href.prevent class="delete" @click="$emit('remove')"><img src="~/assets/images/icons/exit.svg" alt="exit"/></a>
        <div class="row">
            <div class="col-auto pr-2 pr-sm-3">
                <img
                    v-if="colorsGroup.edges[activeColor].node.productimageSet.edges.length > 0"
                    class="photo"
                    :src="colorsGroup.edges[activeColor].node.productimageSet.edges[0].node.imageCropping"
                    alt="product photo"
                />
                <img class="photo" src="~/assets/images/no-photo.jpg" alt="no photo" v-else/>
            </div>
            <div class="col params pr-0">
                <div class="bold name">{{ name }}</div>
                <item-param
                    label="Color"
                    linkName="Change color"
                    :isAvailable="!colorsGroup || !colorsGroup.edges[activeColor].node.isAvailable"
                    @save="
                        $emit('setColor', colorsGroup.edges[activeColor].node.color.id);
                        $emit('setSize', colorsGroup.edges[activeColor].node.sizes.edges[0].node.id);
                    "
                >
                    <template v-slot:activeItem>
                        <div class="color-group">
                            <input type="checkbox" disabled checked id="color"/>
                            <label class="label-color mb-0" for="color">
                                <div
                                    class="color"
                                    :style="
                                        colorsGroup.edges[activeColor].node.color.image
                                            ? 'background-image: url(' +
                                              colorsGroup.edges[activeColor].node.color.image +
                                              ')'
                                            : 'background:' + colorsGroup.edges[activeColor].node.color.color
                                    "
                                ></div>
                            </label>
                        </div>
                    </template>
                    <template v-slot:options>
                        <div class="colors">
                            <div
                                class="color-group"
                                :class="{ opacity: !colorGroup.node.isAvailable }"
                                v-for="(colorGroup, index) in colorsGroup.edges"
                                :key="index"
                            >
                                <input
                                    type="radio"
                                    v-model="activeColor"
                                    @input="activeSize = 0"
                                    :value="index"
                                    :id="colorGroup.node.id"
                                />
                                <label class="label-color mb-0" :for="colorGroup.node.id">
                                    <div
                                        class="color"
                                        :style="
                                            colorGroup.node.color.image
                                                ? 'background-image: url(' + colorGroup.node.color.image + ')'
                                                : 'background:' + colorGroup.node.color.color
                                        "
                                    ></div>
                                </label>
                            </div>
                        </div>
                    </template>
                </item-param>
                <item-param
                    label="Size"
                    linkName="Change size"
                    :isAvailable="
                        colorsGroup.edges[activeColor].node.productsizecolorsizeSet.edges[activeSize].node.count == 0 ||
                        !colorsGroup.edges[activeColor].node.productsizecolorsizeSet.edges[activeSize].node.isAvailable
                    "
                    @save="
                        $emit(
                            'setSize',
                            colorsGroup.edges[activeColor].node.productsizecolorsizeSet.edges[activeSize].node.size.id,
                        )
                    "
                >
                    <template v-slot:activeItem>
                        <div class="bold d-flex align-items-end d-xs-block">
                            {{
                                colorsGroup.edges[activeColor].node.productsizecolorsizeSet.edges[activeSize].node.size
                                    .name
                            }}
                        </div>
                    </template>
                    <template v-slot:options>
                        <div class="sizes">
                            <div
                                class="size-box"
                                v-for="(size, index) in colorsGroup.edges[activeColor].node.productsizecolorsizeSet
                                    .edges"
                                :key="`size ${index}`"
                            >
                                <template v-if="size.node.isAvailable">
                                    <input
                                        type="radio"
                                        v-model="activeSize"
                                        :value="index"
                                        name="sizes"
                                        :disabled="size.node.count == 0"
                                        :id="`size${index}`"
                                    />
                                    <label class="label-size" :for="`size${index}`">{{ size.node.size.name }}</label>
                                </template>
                            </div>
                        </div>
                    </template>
                </item-param>
                <div class="count-group">
                    <a href.prevemt class="control" @click="activeCount > 1 ? activeCount-- : ''">-</a>
                    <input type="text" @input="validate" v-model="activeCount"/>
                    <a
                        href.prevemt
                        class="control"
                        @click="
                            activeCount <
                            colorsGroup.edges[activeColor].node.productsizecolorsizeSet.edges[activeSize].node.count
                                ? activeCount++
                                : ''
                        "
                    >+</a
                    >
                </div>
                <div class="bold mt-30">{{ price }} AED</div>
            </div>
        </div>
    </div>
</template>
<script>
    import ItemParam from './ItemParam.vue';

    export default {
        name: 'BasketItem',
        components: {ItemParam},
        props: {
            name: {
                type: String,
                required: true,
                default: '',
            },
            price: {
                type: Number,
                required: true,
                default: null,
            },
            colorsGroup: {
                type: Object,
                required: false,
                default: null,
            },
            color: {
                type: String,
                default: '',
            },
            size: {
                type: String,
                default: '',
            },
            count: {
                type: Number,
                default: 1,
            },
        },
        data() {
            return {
                activeCount: this.count,
                activeColor: 0,
                activeSize: 0,
            };
        },
        watch: {
            activeCount() {
                this.$emit('setCount', parseInt(this.activeCount));
            },
        },
        created() {
            if (this.color) {
                for (let i in this.colorsGroup.edges) {
                    if (this.colorsGroup.edges[i].node.color.id == this.color) {
                        this.activeColor = i;
                    }
                }
            }
            if (this.size) {
                for (let i in this.colorsGroup.edges[this.activeColor].node.productsizecolorsizeSet.edges) {
                    if (
                        this.colorsGroup.edges[this.activeColor].node.productsizecolorsizeSet.edges[i].node.size.id ==
                        this.size
                    ) {
                        this.activeSize = i;
                    }
                }
            }
        },
        methods: {
            validate() {
                if (this.activeCount * 1 + 0 != this.activeCount || !this.activeCount) {
                    this.activeCount = 1;
                } else if (
                    this.activeCount >
                    this.colorsGroup.edges[this.activeColor].node.productsizecolorsizeSet.edges[this.activeSize].node
                        .count
                ) {
                    this.activeCount = this.colorsGroup.edges[this.activeColor].node.productsizecolorsizeSet.edges[
                        this.activeSize
                        ].node.count;
                }
            },
        },
    };
</script>
<style lang="less">
    .params {
        .link-grey {
            @media @xs {
                font-size: 12px;
            }
        }
    }
</style>
<style lang="less" scoped>
    .item-group {
        position: relative;
        padding: 15px 30px 15px 15px;
        background: @white;
        margin-bottom: 15px;

        @media @xs {
            padding: 0px;
        }

        .delete {
            display: flex;
            position: absolute;
            right: 15px;
            top: 15px;
            z-index: 100;
            cursor: pointer;

            @media @xs {
                top: 0px;
                right: 0;
            }

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

                @media @xs {
                    font-size: 14px;
                }

                &.name {
                    line-height: 15px;
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
                width: 20px;
                height: 20px;

                .label-color {
                    width: 100%;
                    height: 100%;

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

            .sizes {
                .size-box {
                    margin-right: 10px;

                    .label-size {
                        min-width: 20px;
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
