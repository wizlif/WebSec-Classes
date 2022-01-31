<template>
  <v-row no-gutters justify="center" align-content="center" style="height: 100vh;background: #BC4B4A">
    <img :src="image" style="height: 100vh"/>
  </v-row>
</template>

<script>

export default {
  name: 'Home',
  data(){
    return {
      image: require('@/assets/mj.gif')
    }
  }
}
</script>
