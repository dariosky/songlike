<template>
  <div>
    <div v-if="!loading">
      <p>You logged out from this browser.</p>
      <p>Spotlike will continue doing its magic to your account.</p>
    </div>
    <div v-else>
      <v-progress-circular indeterminate color="primary"></v-progress-circular>
    </div>
    <div v-if="error">
      {{ error }}
    </div>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios, store }) {
    return await $axios
      .$post('/logout')
      .then((response) => {
        store.commit('user/login', { id: null })
        return {
          loading: false,
          error: null,
        }
      })
      .catch((err) => {
        if (err.response && err.response.status === 401) {
          return {
            error: err.response.data,
            loading: false,
          }
        }
      })
  },
  data() {
    return {
      loading: true,
      error: null,
    }
  },
  mounted() {
    if (!this.$store.state.user.id)
      setTimeout(() => this.$router.push('/'), 3000)
  },
}
</script>
