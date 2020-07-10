<template>
  <section>
    <div class="columns">
      <div class="hero-body" :style="{ 'background-image': item.largeImgSrc }">
        <div class="vertical-align">
          <h1 class="title">{{ item.title }}</h1>
          <h4 class="subtitle">
            <p class="subtitle-tag">{{ item.duration }} |</p>
            <p class="subtitle-tag">{{ item.genre }} |</p>
            <p class="subtitle-tag">{{ item.releaseDate }}</p>
          </h4>
          <p class="description">{{ item.description }}</p>
          <div class="links">
            <a class="favorites-button" @click="addToFavorites()">
              <span v-if="!item.favorite">Add to</span>
              <span v-else>Remove from</span>
              favorites
              <i class="fa fa-plus-square-o"></i>
            </a>
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
          largeImgSrc: `url('https://image.tmdb.org/t/p/w500/phxiKFDvPeQj4AbkvJLmuZEieDU.jpg')`,
          smallImgSrc:
            "https://image.tmdb.org/t/p/w185/cCTJPelKGLhALq3r51A9uMonxKj.jpg",
          releaseDate: "July 21 2017",
          duration: "1hr 46min",
          genre: "Action, Drama, History",
          trailerPath: "https://www.youtube.com/embed/F-eMt3SrfFU",
          favorite: false
        };
      }
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
  },
  methods: {
    addToFavorites() {
      this.item.favorite = !this.item.favorite;
    }
  }
};
</script>

<style scoped>
.hero-body {
  background-color: rgba(0, 0, 0, 0.7);
  background-blend-mode: multiply;
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