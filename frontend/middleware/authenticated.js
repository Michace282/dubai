export default function ({ store, error }) {
    if (!store.state.user.user) {
        return error({ statusCode: 404 });
    }
}
