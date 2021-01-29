<template>
    <div class="filter">
        <div class="mobile-head">
            <div class="filter-caption">
                Filter
                <img src="~/assets/images/icons/filter.svg" />
            </div>
            <a href.prevent @click="$emit('closeFilter')">
                <img src="~/assets/images/icons/exit.svg" />
            </a>
        </div>
        <filter-accordion class="arrow-descktop-hide" name="Ladies" title="Ladies" visible>
            <div class="category-box">
                <ul class="categories">
                    <li class="category active">Body</li>
                    <li class="category">Blouses</li>
                </ul>
            </div>
        </filter-accordion>
        <filter-accordion class="mt-30" name="price" title="Price range">
            <div class="d-flex align-items-center">
                <input placeholder="Min" class="filter-input" />
                <span class="hyphen">-</span>
                <input placeholder="Max" class="filter-input" />
            </div>
        </filter-accordion>
        <filter-accordion class="mt-30" title="Colors" name="colors">
            <div class="colors">
                <div class="color-group">
                    <input type="checkbox" true-value="true" id="color" />
                    <label class="label-color" for="color">
                        <div class="color"></div>
                    </label>
                </div>
            </div>
        </filter-accordion>
        <filter-accordion class="mt-30" title="Size" name="size">
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
        </filter-accordion>
        <div class="btn-box">
            <button class="btn btn-black w-100 mt-45">filter</button>
            <button class="btn btn-outline-black w-100 mt-30">reset the filter</button>
        </div>
    </div>
</template>
<script>
    import FilterAccordion from './FilterAccordion.vue';

    export default {
        name: 'FilterCatalog',
        components: { FilterAccordion },
        data() {
            return {};
        },
    };
</script>
<style lang="less" scoped>
    .btn {
        padding: 11px 15px;

        @media @large {
            max-width: 155px;
            margin: 0px;
            font-size: 14px;
            padding: 9px 14px;
        }

        @media (max-width: 320px) {
            max-width: 100%;
            width: 100%;
            &:not(:first-child) {
                margin-top: 20px;
            }
        }
    }

    .btn-box {
        @media @large {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-direction: row-reverse;
            padding: 0px 20px;
            margin-top: 45px;
        }

        @media (max-width: 320px) {
            display: block;
        }
    }

    .mobile-head {
        display: none;

        @media @large {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 30px 20px;
        }
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

    .color-group {
        margin-right: 15px;
    }

    .colors {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        justify-content: flex-start;
    }

    .filter-input {
        max-width: 110px;
        width: 100%;
        font-family: 'Inter-Light';
        font-size: 14px;
        color: @grey4;
        padding: 4px 10px;
        background: @white;
        border: 1px solid @black;
        box-sizing: border-box;
        border-radius: 2px;

        @media @large {
            max-width: 154px;
        }
    }

    .hyphen {
        margin: 0px 15px;
        font-weight: bold;
        color: @black;

        @media @large {
            margin: 0px 10px;
        }
    }

    .categories {
        &:not(:first-child) {
            margin-top: 15px;
        }
        padding-left: 10px;
        text-decoration: none;
        list-style: none;

        .category {
            cursor: pointer;
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
</style>
