<template>
  <section>
    <div class="header">
      <div class="poster-wrapper">
        <img class="poster" :src="resolve_img_url(item.poster_path)" :alt="item.title" />
      </div>
      <div class="movie-info-part">
        <div class="movie-info">
          <div class="key-info">
            <h2 class="movie-title">
              {{item.title}}
              <span class="tagline">{{item.tagline}}</span>
            </h2>
            <div class="general-info">
              <span class="release-date">{{item.releaseDate}}</span>
              <span class="genres">{{genres}}</span>
              <span class="runtime">{{item.duration}}</span>
            </div>
          </div>
          <div class="user-interaction">
            <div class="score-section">
              <div class="user-avg-score">
                <span class="movie-score">{{item.vote_average}}</span>
              </div>
              <span class="score-section-text">
                Average
                <br />User Score
              </span>
            </div>
            <div class="score-section favorite-button">
              <a-button type="primary" shape="circle" icon="star" :size="size" />
            </div>
            <div class="play-trailer score-section">
              <a :href="resolve_video_url(item.trailer_key)">
                <a-icon type="play-circle" />Play Trailer
              </a>
            </div>
          </div>
          <div class="detailed-info">
            <h3>Overview:</h3>
            <div class="movie-overview">
              <!-- <p>{{item.description}}</p> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "MovieSynopsis",
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
.header {
  display: flex;
  flex-wrap: nowrap;
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
  /* display: flex;
  flex-wrap: wrap; */
}
.movie-title {
  width: 100%;
  margin: 0;
  padding: 0;
  font-size: 2.2rem;
  font-weight: 700;
}
.tagline {
  margin: 0;
  padding: 0;
  font-weight: 350;
  font-size: 1.3rem;
  font-style: italic;
  opacity: 0.7;
}
.general-info {
  display: flex;
}
.release-date {
  padding-left: 20px;
  position: relative;
  top: 0;
  left: 0;
}
.genres {
  padding-left: 20px;
  position: relative;
  top: 0;
  left: 0;
}
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

.hero-body {
  background-color: rgba(0, 34, 95, 0.8);
  background-blend-mode: color;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  padding-bottom: 4rem !important;
  padding-top: 4.5rem !important;
}
.home-intro {
  font-size: 60px;
  letter-spacing: 8px;
  color: red;
  text-align: center;
  text-transform: uppercase;
}
.title {
  font-size: 45px;
  font-weight: 600;
  color: white;
}
.subtitle {
  font-size: 15px;
  font-weight: 600;
  color: red;
}
.subtitle-tag {
  display: inline;
}
.description {
  font-size: 15px;
  margin-bottom: 24px;
  max-width: 450px;
}
.favorites-button {
  text-decoration: none;
  color: #fff;
}
.favorites-button:hover {
  color: goldenrod;
}
.fa-plus-square-o {
  padding-left: 10px;
  padding-top: 2px;
}
.columns {
  padding: 20px;
  padding-bottom: 30px;
  text-align: center;
  /* background: #1e1d1d !important; */
  /* position: relative; */
  /* box-shadow: 0 0 50px 5px rgba(0, 0, 0, 0.25); */
  /* background: linear-gradient(to bottom right, #7d1e24, #bb2d35); */
}
.vertical-align {
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  flex-direction: column;
  align-items: center;
  -webkit-align-items: center;
  justify-content: center;
  -webkit-justify-content: center;
}
</style>