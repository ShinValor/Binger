<template>
  <div
    class="header"
    :style="{
      'background-image': 'url(' + imgUrl(movie.backdrop_path) + ')'
    }"
  >
    <div class="header-contents fontColor">
      <div class="poster-wrapper">
        <img
          class="poster"
          :src="imgUrl(movie.poster_path)"
          :alt="movie.title"
        />
      </div>
      <div class="movie-info-part">
        <div class="movie-info">
          <div class="key-info">
            <div class="title-wrapper left-align">
              <h2 class="movie-title left-align fontColor">
                {{ movie.title }}
              </h2>
              <span class="tagline">{{ movie.tagline }}</span>
            </div>
            <div class="general-info">
              <span class="release-date">{{ releaseDate() }}</span>
              <span class="genres">{{ genres() }}</span>
              <span class="runtime">{{ runtime(movie.runtime) }}</span>
            </div>
          </div>
          <div class="movie-rating">
            <div class="score-section">
              <div class="user-avg-score">
                <span class="movie-score">{{ movie.vote_average }}</span>
              </div>
              <span class="score-section-text">
                Average
                <br />
                User Score
              </span>
            </div>
            <div class="favorite-btn">
              <a-button
                class="like-btn"
                type="primary"
                shape="circle"
                icon="like"
                @click="likeMovie(movie)"
              />
              <a-button
                class="dislike-btn"
                type="primary"
                shape="circle"
                icon="dislike"
                @click="dislikeMovie(movie)"
              />
            </div>
          </div>
          <div class="detailed-info left-align">
            <h1 class="text-overview fontColor">Overview</h1>
            <div class="play-trailer">
              <a
                class="trailer-btn"
                :href="vidUrl(movie.trailer_key)"
                target="_blank_"
              >
                <a-icon type="play-circle" :style="{ color: '#ff0000' }" />
                Play Trailer
              </a>
            </div>
            <div class="movie-overview" dir="auto">
              <p class="movie-overview-text">{{ movie.overview }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "MovieOverview",
  data() {
    return {
      movie: {},
      errors: []
    };
  },
  props: {
    movieID: {
      type: Number,
      required: true
    }
  },
  created() {
    axios
      .get("https://binger-api-testv1.azurewebsites.net/movie/" + this.movieID)
      .then(res => {
        this.movie = res.data;
      })
      .catch(err => {
        this.error = err;
      })
      .finally(() => (this.loading = false));
  },
  methods: {
    imgUrl(path) {
      return "https://image.tmdb.org/t/p/w342" + path;
    },
    vidUrl(path) {
      return "https://www.youtube.com/watch?v=" + path;
    },
    genres() {
      return typeof this.movie.genres !== "undefined"
        ? this.movie.genres.join(", ")
        : "";
    },
    releaseDate() {
      const msec = Date.parse(this.movie.release_date);
      const date = new Date(msec);
      return date.toLocaleString("default", {
        year: "numeric",
        month: "long",
        day: "numeric"
      });
    },
    runtime(num) {
      const hours = num / 60;
      const rhours = Math.floor(hours);
      const minutes = Math.round((hours - rhours) * 60);
      return rhours + "hr " + minutes + " min";
    },
    likeMovie(movie) {
      this.$store.dispatch("likeMovie", movie);
      this.$message.success(`You liked ${movie.title}`);
    },
    dislikeMovie(movie) {
      this.$store.dispatch("dislikeMovie", movie);
      this.$message.error(`You disliked ${movie.title}`);
    }
  }
};
</script>

<style scoped>
.left-align {
  text-align: left;
}

.header {
  display: flex;
  flex-wrap: nowrap;
  padding-bottom: 4rem !important;
  padding-top: 4.5rem !important;
  background-color: #2a323d;
  background-blend-mode: multiply;
  background-size: cover;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}

.header-contents {
  margin: 2em;
  display: flex;
  flex-wrap: nowrap;
}

.poster-wrapper {
  min-width: 300px;
  width: 300px;
  height: 450px;
  display: block;
  position: relative;
  top: 0;
  left: 0;
}

.poster {
  width: 100%;
  min-width: 100%;
  height: 100%;
  min-height: 100%;
  display: block;
  border-width: 0px;
  outline: none;
}

.movie-info-part {
  display: flex;
}

.movie-info {
  padding-left: 40px;
}

.key-info {
  margin-bottom: 10px;
  width: 100%;
}

.movie-title {
  margin: 0;
  padding: 0;
  display: inline;
  font-size: 2.2rem;
  font-weight: 700;
}

.tagline {
  margin: 0;
  padding: 0 0 0 15px;
  display: inline;
  font-weight: 350;
  font-size: 1.3rem;
  font-style: italic;
  opacity: 0.7;
}

.general-info {
  display: flex;
  justify-content: left;
}

.release-date,
.genres,
.runtime {
  margin-right: 20px;
  position: relative;
  top: 0;
  left: 0;
}

.movie-rating {
  margin-bottom: 20px;
  display: flex;
  justify-content: left;
  align-items: center;
  text-align: left;
}

.score-section {
  margin-right: 10px;
  display: flex;
  justify-content: left;
}

.play-trailer {
  box-sizing: border-box;
  margin: 0 0 10px;
  display: inline-flex;
  align-items: left;
  justify-content: left;
}

.trailer-btn {
  display: inline-block;
  vertical-align: middle;
  color: white;
  font-size: 1.3em;
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  transform: perspective(1px) translateZ(0);
  -webkit-transform: perspective(1px) translateZ(0);
  transition-duration: 0.3s;
  -webkit-transition-duration: 0.3s;
  transition-property: transform;
  -webkit-transition-property: transform;
  transition-timing-function: ease-out;
  -webkit-transition-timing-function: ease-out;
}

.trailer-btn:hover {
  transform: scale(1.1);
}

.movie-score {
  margin-right: 10px;
  font-size: 30px;
  font-weight: 600;
}

.score-section-text {
  margin-right: 5px;
  font-weight: 700;
  font-size: 14px;
  white-space: pre-line;
}

.movie-overview-text {
  text-align: left;
  font-size: 1.2em;
}

.text-overview {
  margin: 10px 20px 10px 0;
  display: inline;
  font-weight: 600;
  font-size: 2.2em;
}

.fontColor {
  color: ivory;
}

.like-btn,
.dislike-btn {
  margin-left: 15px;
  background-color: #222831;
  border-color: white;
}

.like-btn:hover,
.dislike-btn:hover {
  background-color: white;
  color: #222831;
  transform: scale(1.2);
}

.like-btn:active,
.dislike-btn:active {
  background-color: #222831;
  color: white;
}

@media only screen and (max-width: 600px) {
  .header-contents,
  .tagline,
  .movie-title {
    display: block;
  }

  .tagline {
    margin-top: -10px;
    padding: 0;
  }

  .title-wrapper {
    margin-bottom: 10px;
  }

  .general-info {
    text-align: left;
  }

  .release-date {
    padding-left: 0px;
  }

  .poster-wrapper {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
