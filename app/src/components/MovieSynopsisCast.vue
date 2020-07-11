<template>
  <div class="cast">
    <div class="image">
      <a-avatar
        :size="64"
        icon="user"
        style="margin-right: 8px"
        :src="resolve_img_url(cast.profile_path)"
      />
    </div>
    <div class="content">
      <p>
        <strong>{{cast.name}}</strong>
        <br />
        {{cast.character}}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieSynopsisCast",
  props: {
    cast: {
      type: Object,
      default: function() {
        return {
          cast_id: 4,
          character: "The Narrator",
          credit_id: "52fe4250c3a36847f80149f3",
          gender: 2,
          id: 819,
          name: "Edward Norton",
          order: 0,
          profile_path: "/eIkFHNlfretLS1spAcIoihKUS62.jpg"
        };
      }
    }
  },
  methods: {
    resolve_img_url: function(path) {
      return "https://image.tmdb.org/t/p/w342" + path;
    }
  }
};
</script>

<style scoped>
.cast {
  height: 100%;
  padding-top: 10px;
  background: #e6ecf1;
  max-width: 500px;
  margin: 0 auto;
  padding-bottom: 15px;
}

.box {
  margin-bottom: 0;
  border-radius: 0;
}

.content {
  align-content: center;
  display: inline-block;
  padding: 10px;
}

.image {
  display: inline-block;
  margin: 2px;
}
</style>