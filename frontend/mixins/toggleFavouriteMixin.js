export default {
    mounted() {
        let id = this.id ? this.id : this.$route.params.slug;
        if (sessionStorage.getItem('isFavourite' + id) != null) {
            this.isFavorite = sessionStorage.getItem('isFavourite' + id) == 'true';
        }
    },
    methods: {
        toggleFavouriteMixin(id, isFavorite) {
            if (isFavorite) {
                this.$apollo
                    .mutate({
                        mutation: require('~/graphql/mutations/favourite/productWishlistDelete.graphql'),
                        variables: {
                            guestUuid: this.$store.state.user.guestUuid,
                            product: id,
                        },
                    })
                    .then((data) => {
                        if (data && data.data.productWishlistDelete.errors.length == 0) {
                            this.isFavorite = false;
                            sessionStorage.setItem('isFavourite' + id, false);
                            this.$emit('remove');
                        } else {
                            this.$bvToast.toast(data.data.productWishlistDelete.errors[0].messages, {
                                title: 'Favourites',
                                variant: 'danger',
                            });
                        }
                    });
            } else {
                this.$apollo
                    .mutate({
                        mutation: require('~/graphql/mutations/favourite/productWishlistCreate.graphql'),
                        variables: {
                            guestUuid: this.$store.state.user.guestUuid,
                            product: id,
                        },
                    })
                    .then((data) => {
                        if (data && data.data.productWishlistCreate.errors.length == 0) {
                            this.isFavorite = true;
                            sessionStorage.setItem('isFavourite' + id, true);
                        } else {
                            this.$bvToast.toast(data.data.productWishlistCreate.errors[0].messages, {
                                title: 'Favourites',
                                variant: 'danger',
                            });
                        }
                    });
            }
        },
    },
};
