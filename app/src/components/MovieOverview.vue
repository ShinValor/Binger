<template>
  <section>
    <div
      class="header"
      :style="{
        'background-image': 'url(' + resolve_img_url(item.backdrop_path) + ')'
      }"
    >
      <div class="header-contents fontColor">
        <div class="poster-wrapper">
          <img
            class="poster"
            :src="resolve_img_url(item.poster_path)"
            :alt="item.title"
          />
        </div>
        <div class="movie-info-part">
          <div class="movie-info">
            <div class="key-info">
              <div class="title-wrapper left-align">
                <h2 class="movie-title left-align fontColor">
                  {{ item.title }}
                </h2>
                <span class="tagline">{{ item.tagline }}</span>
              </div>
              <div class="general-info">
                <span class="release-date">{{ releaseDate() }}</span>
                <span class="genres">{{ genres() }}</span>
                <span class="runtime">{{ runtime(item.runtime) }}</span>
              </div>
            </div>
            <div class="user-interaction left-align">
              <div class="score-section">
                <div class="user-avg-score">
                  <span class="movie-score">{{ item.vote_average }}</span>
                </div>
                <span class="score-section-text">
                  Average
                  <br />User Score
                </span>
              </div>
              <div class="score-section favorite-button">
                <a-button type="primary" shape="circle" icon="star" />
              </div>
              <div class="play-trailer score-section">
                <a :href="resolve_video_url(item.trailer_key)">
                  <a-icon type="play-circle" />Play Trailer
                </a>
              </div>
            </div>
            <div class="detailed-info left-align">
              <h3 class="text-overview fontColor">Overview:</h3>
              <div class="movie-overview" dir="auto">
                <p class="movie-overview-text">{{ item.overview }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
export default {
  name: "MovieOverview",
  props: {
    movieID: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      item: Object,
      errors: []
    };
  },
  methods: {
    addToFavorites() {
      this.item.favorite = !this.item.favorite;
    },
    resolve_img_url(path) {
      return "https://image.tmdb.org/t/p/w342" + path;
    },
    resolve_video_url(path) {
      return "https://www.youtube.com/watch?v=" + path;
    },
    genres() {
      return typeof this.item.genres !== "undefined"
        ? this.item.genres.join(", ")
        : "";
    },
    releaseDate() {
      const msec = Date.parse(this.item.release_date);
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
    }
  },
  created() {
    axios
      .get("http://0.0.0.0:5000/movie/" + this.movieID)
      .then(res => {
        this.item = res.data;
      })
      .catch(err => {
        this.error = err;
      })
      .finally(() => (this.loading = false));
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
  background-color: rgba(0, 34, 95, 0.7);
  background-blend-mode: multiply;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  padding-bottom: 4rem !important;
  padding-top: 4.5rem !important;
}

.header-contents {
  display: flex;
  flex-wrap: nowrap;
  margin: 2em;
}

.poster-wrapper {
  display: block;
  min-width: 300px;
  width: 300px;
  height: 450px;
  position: relative;
  top: 0;
  left: 0;
}

.poster {
  display: block;
  width: 100%;
  min-width: 100%;
  height: 100%;
  min-height: 100%;
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
  width: 100%;
  margin-bottom: 24px;
}
.movie-title {
  margin: 0;
  padding: 0;
  font-size: 2.2rem;
  font-weight: 700;
  display: inline;
}

.tagline {
  margin: 0;
  padding: 0;
  font-weight: 350;
  font-size: 1.3rem;
  font-style: italic;
  opacity: 0.7;
  display: inline;
  padding-left: 15px;
}

.general-info {
  display: flex;
}

.release-date,
.genres,
.runtime {
  padding-left: 20px;
  position: relative;
  top: 0;
  left: 0;
}
.score-section {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  height: 68px;
  margin-right: 20px;
}

.movie-score {
  font-size: 30px;
  font-weight: 600;
}

.score-section-text {
  font-weight: 700;
  margin-left: 6px;
  white-space: pre-line;
  font-size: 14px;
}

.movie-overview-text {
  text-align: left;
}

.text-overview {
  font-weight: 600;
  font-size: 1.3em;
}

.fontColor {
  color: ivory;
}

@media only screen and (max-width: 600px) {
  .header-contents,
  .tagline,
  .movie-title {
    display: block;
  }

  .tagline {
    margin-top: -10px;
    padding-left: 15px;
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
