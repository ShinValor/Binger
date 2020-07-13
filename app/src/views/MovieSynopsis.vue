<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
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
                <span class="release-date">{{ item.releaseDate }}</span>
                <span class="genres">{{ genres }}</span>
                <span class="runtime">{{ item.duration }}</span>
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
                <p class="movie-overview-text">{{ item.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <MovieSynopsisMovieList listType="Similar Movies" />
    <MovieSynopsisCastList />
  </a-layout>
</template>

<script>
import MovieSynopsisMovieList from "@/components/MovieSynopsisMovieList.vue";
import MovieSynopsisCastList from "@/components/MovieSynopsisCastList.vue";

export default {
  name: "MovieSynopsis",
  components: {
    MovieSynopsisMovieList,
    MovieSynopsisCastList
  },
  props: {
    movie: {
      type: Object,
      default: function() {
        return JSON.parse(
          '{ "id": 1654,"trailerPath": "https://www.youtube.com/embed/ff1V6ywnWcY", "genres": [ "Action", "Adventure", "War"], "overview": "12 American military prisoners in World War II are ordered to infiltrate a well-guarded enemy ch\u00e2teau and kill the Nazi officers vacationing there. The soldiers, most of whom are facing death sentences for a variety of violent crimes, agree to the mission and the possible commuting of their sentences.", "popularity": 7.7, "poster_path": "https://image.tmdb.org/t/p/w500/iFpgjfE4gt7guOLvrqgZZoO4Rjk.jpg", "release_year": "1967", "score": 0, "title": "The Dirty Dozen", "is_movie": true }'
        );
      }
    },
    item: {
      type: Object,
      default: function() {
        return {
          id: "Dark Phoenix",
          title: "Dark Phoenix",
          subtitle: "Dark Phoenix",
          description: `The X-Men face their most formidable and powerful foe when one of their own, Jean Grey, starts to spiral out of control. During a rescue mission in outer space, Jean is nearly killed when she's hit by a mysterious cosmic force. Once she returns home, this force not only makes her infinitely more powerful, but far more unstable. The X-Men must now band together to save her soul and battle aliens that want to use Grey's new abilities to rule the galaxy.`,
          backdrop_path: "/phxiKFDvPeQj4AbkvJLmuZEieDU.jpg",
          poster_path: "/cCTJPelKGLhALq3r51A9uMonxKj.jpg",
          releaseDate: "July 21 2017",
          duration: "1hr 46min",
          genre: ["Action", "Drama", "History"],
          trailerPath: "https://www.youtube.com/embed/F-eMt3SrfFU",
          favorite: false,
          vote_average: 6.0,
          tagline: "The phoenix will rise",
          trailer_key: "QWbMckU3AOQ"
        };
      }
    }
  },
  computed: {
    genres: function() {
      return this.item.genre.join(", ");
    }
  },
  methods: {
    addToFavorites() {
      this.item.favorite = !this.item.favorite;
    },
    resolve_img_url: function(path) {
      return "https://image.tmdb.org/t/p/w342" + path;
    },
    resolve_video_url: function(path) {
      return "https://www.youtube.com/watch?v=" + path;
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
