<template>
    <div>
        Hello Yogesh {{ username }}. <br>
        Welcome to your dashboard.
    </div>
</template>
<script>
export default {
    data() {
        return {
            username: this.$store.state.user.name
        }
    }
}

</script>