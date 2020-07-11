<template>
  <div class="cast">
    <div class="tweet">
      <article class="media">
        <div class="media-left">
          <figure class="image is-64x64">
            <a-avatar :size="64" icon="user" />
          </figure>
        </div>
        <div class="media-content">
          <div class="content">
            <p>
              <strong>{{cast.name}}</strong>
              <small>{{tweet.handle}}</small>
              <br />
              {{cast.character}}
            </p>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieSynopsisCast",
  props: {
    cast: Object
  }
};
</script>

<style scoped>
.cast {
  height: 100%;
  padding-top: 10px;
  background: #e6ecf1;
}

.tweet {
  max-width: 500px;
  margin: 0 auto;
  padding-bottom: 15px;
}

.box {
  margin-bottom: 0;
  border-radius: 0;
}

.content small {
  color: #00d1b2;
}

img {
  border-radius: 30px;
}
</style>