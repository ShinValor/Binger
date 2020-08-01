<template>
  <li class="movie-list">
    <img class="poster" :src="imgUrl(item.poster_path)" />
    <br />
    <div>
      <a class="title">{{ item.title }}</a>
      <div class="d-flex items-center area muted">
        <p class="para-tag">{{ item.release_year }}</p>
        <p class="separator genres para-tag">{{ genres }}</p>
      </div>
      <p class="area plot para-tag">{{ item.overview }}</p>
      <div class="d-flex items-center area">
        <p class="rating para-tag" title="Rating" v-show="item.popularity">
          <span class="rating-star"></span>
          {{ item.vote_average }}
        </p>
      </div>
    </div>
  </li>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  methods: {
    imgUrl(path) {
      return "https://image.tmdb.org/t/p/w342" + path;
    }
  },
  computed: {
    genres: function() {
      var _genres = [];
      this.item.genres.forEach(function(genre) {
        _genres.push(genre);
      });
      return _genres.join(", ");
    }
  }
};
</script>

<style scoped>
.area {
  margin-top: 0.5em;
}

.d-flex {
  display: flex;
}

.d-flex.items-center {
  align-items: center;
}

.separator::before {
  color: #ddd;
  margin-left: 0.3em;
  margin-right: 0.3em;
  content: "|";
}

.movie-list {
  background-color: #222831;
  display: flex;
  align-items: flex-start;
  padding: 1em;
}

.movie-list:hover {
  background-color: #2a313c;
}

.poster {
  height: 170px;
  margin-right: 1em;
}

.muted {
  font-size: 0.8em;
  color: #999;
}

.para-tag {
  margin: 0;
}

.title {
  font-size: 1.2em;
  color: white;
}

.plot {
  color: white;
}

.rating {
  /* color: #666; */
  color: white;
  font-size: 0.9em;
  display: flex;
  align-items: center;
}

.rating-star {
  background: url(https://m.media-amazon.com/images/G/01/imdb/images/listo/sprite-2426358703._V_.png)
    no-repeat 0 -241px;
  display: inline-block;
  height: 12px;
  margin-right: 0.3em;
  vertical-align: middle;
  width: 12px;
}
</style>
