<template>
  <div>
    <p>
      Connect your Spotify account to add several smart features around your
      listening habits and automate some of the boring tasks.
    </p>

    <div v-if="$store.state.user.authUrl">
      <a :href="$store.state.user.authUrl" class="button action">
        <img id="spotify-logo" src="@/assets/spotify.svg" alt="" />
        Log in with Spotify
      </a>
    </div>

    <div v-if="user.id">
      Your {{ user.name }}
      <img :src="userPicture" alt="" class="spotify-profile-pitcture" />
      account is connected - the magic will happen.
    </div>

    <h2>Here is what it does</h2>
    <ul>
      <li>
        Syncs all of the songs you like to a playlist - so that you can share
        them with others.
      </li>

      <li>
        Looks for duplicates in your liked songs, and only keeps the oldest.
      </li>
    </ul>
  </div>
</template>

<script>
import anonymousPicture from 'assets/anonymous-user.svg'

export default {
  computed: {
    user() {
      return this.$store.state.user
    },
    userPicture() {
      return this.$store.state.user.picture || anonymousPicture
    },
  },
  head: {
    title: 'Automated tasks for your Spotify playlists',
  },
}
</script>

<style scoped>
.button {
  display: inline-block;
  padding: 10px 30px;
  text-decoration: none;
  border: 1px solid black;
  margin: 10px auto;
  font-size: 1.3em;
  border-radius: 6px;
}

.action {
  background-color: #3a833a;
  color: white;
}

#spotify-logo {
  margin-right: 10px;
  width: 32px;
  height: 32px;
  vertical-align: middle;
}

.spotify-profile-pitcture {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  vertical-align: middle;
}
</style>
