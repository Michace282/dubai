<template>
    <div class="navbar-box">
        <div class="container">
            <b-navbar toggleable="lg" type="dark">
                <b-navbar-brand to="/"><img src="~/assets/images/logo.png" /></b-navbar-brand>

                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

                <b-collapse id="nav-collapse" is-nav>
                    <b-navbar-nav class="links m-auto">
                        <b-nav-item to="#">New <img class="star" src="../assets/images/icons/star.png" /></b-nav-item>
                        <b-nav-item to="#">Ladies</b-nav-item>
                        <b-nav-item to="#">Mens</b-nav-item>
                        <b-nav-item to="#">Dance shoes</b-nav-item>
                        <b-nav-item to="#">Accessories</b-nav-item>
                        <b-nav-item to="/about-us/">About us</b-nav-item>
                        <b-nav-item to="/contacts/">Contact us</b-nav-item>
                    </b-navbar-nav>

                    <b-navbar-nav class="ml-auto icons">
                        <b-nav-item to="#"><img src="../assets/images/icons/heart.svg" /></b-nav-item>
                        <b-nav-item to="#"><img src="../assets/images/icons/loop.svg" /></b-nav-item>
                        <b-nav-item to="#"><img src="../assets/images/icons/basket.svg" /></b-nav-item>
                        <b-nav-item to="#" @click="$emit('showRegModal')"
                            ><img src="../assets/images/icons/account.svg"
                        /></b-nav-item>
                    </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'TheNavbar',
    };
</script>
<style lang="less" scoped>
    @import '../assets/css/colors.less';
    .navbar-box {
        background: @black;
    }
</style>
