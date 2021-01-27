<template>
    <div>
        <div class="category-box">
            <div class="title">Ladies</div>
            <ul class="categories">
                <li class="category active">Body</li>
                <li class="category">Blouses</li>
            </ul>
        </div>
        <filter-card class="mt-30" name="price" title="Price range">
            <div class="d-flex align-items-center">
                <input placeholder="Min" class="filter-input" />
                <span class="hyphen">-</span>
                <input placeholder="Max" class="filter-input" />
            </div>
        </filter-card>
        <filter-card class="mt-30" title="Colors" name="colors">
            <div class="colors">
                <div class="color-box">
                    <input type="checkbox" true-value="true" id="color" />
                    <label class="label-color" for="color">
                        <div class="color"></div>
                    </label>
                </div>
            </div>
        </filter-card>
        <filter-card class="mt-30" title="Size" name="size">
            <div class="sizes">
                <div class="size-box">
                    <input type="checkbox" true-value="true" id="size3" />
                    <label class="label-size" for="size3">XS</label>
                </div>
                <div class="size-box">
                    <input type="checkbox" true-value="true" id="size2" />
                    <label class="label-size" for="size2">S</label>
                </div>
            </div>
        </filter-card>
        <button class="btn btn-black w-100 mt-45">
            filter
        </button>
        <button class="btn btn-outline-black w-100 mt-30">
            reset the filter
        </button>
    </div>
</template>
<script>
    import FilterCard from './FilterCard.vue';

    export default {
        name: 'FilterCatalog',
        components: { FilterCard },
        data() {
            return {};
        },
    };
</script>
<style lang="less" scoped>
    @import '../../assets/css/variables';

    .btn {
        padding: 11px 15px;
    }

    .sizes {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        justify-content: flex-start;

        .size-box {
            margin-right: 15px;
            input {
                display: none;

                &:checked + label {
                    font-family: 'Inter-Medium';
                    background: @black;
                    color: @white;
                }
            }

            .label-size {
                width: 30px;
                height: 30px;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                font-size: 14px;
                font-family: 'Inter-Light';
                color: @black;
                background: @white;
                border: 1px solid @black;
                box-sizing: border-box;
                border-radius: 2px;
                line-height: 17px;
            }
        }
    }

    .colors {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        justify-content: flex-start;

        .color-box {
            margin-right: 15px;

            input {
                display: none;

                &:checked + .label-color {
                    border-color: @black;
                }
            }

            .label-color {
                width: 30px;
                height: 30px;
                border: 1px solid @grey2;
                box-sizing: border-box;
                border-radius: 50%;
                padding: 2px;
                cursor: pointer;

                .color {
                    width: 100%;
                    height: 100%;
                    background: red;
                    border-radius: 50%;
                }
            }
        }
    }

    .title {
        font-family: 'Inter-Medium';
        font-size: 24px;
        color: @black;
    }

    .filter-input {
        max-width: 110px;
        font-family: 'Inter-Light';
        font-size: 14px;
        color: @grey4;
        padding: 4px 10px;
        background: @white;
        border: 1px solid @black;
        box-sizing: border-box;
        border-radius: 2px;
    }

    .hyphen {
        margin: 0px 15px;
        font-weight: bold;
        color: @black;
    }

    .category-box {
        &:not(:first-child) {
            margin-top: 15px;
        }

        .categories {
            padding-left: 10px;
            text-decoration: none;
            list-style: none;

            .category {
                margin-top: 5px;
                line-height: 22px;
                font-family: 'Inter-Light';
                font-size: 18px;
                color: @black;

                &.active {
                    font-family: 'Inter-Regular';
                    color: @yellow;
                }
            }
        }
    }
</style>
