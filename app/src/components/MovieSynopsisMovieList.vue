<template>
  <div class="card">
    <h2 class="carousel-type-text">{{ listType }}</h2>
    <flickity class="carousel" ref="flickity" :options="flickityOptions">
      <div
        class="carousel-cell"
        v-for="item in MovieList"
        v-bind:key="item.title"
      >
      <div class="carousel-cell" v-for="(item, index) in MovieList" v-bind:key="index">
        <router-link :to="{ name: 'MovieSynopsis', params: { id: item.id } }">
          <img class="carousel-cell-image" :src="resolve_img_url(item.poster_path, item.title)" />
        </router-link>
      </div>
    </flickity>
  </div>
</template>
<script>
import Flickity from "vue-flickity";

export default {
  name: "MovieSynopsisMovieList",
  components: {
    Flickity
  },
  data() {
    return {
      flickityOptions: {
        initialIndex: 0,
        autoPlay: 3000,
        groupCells: 5,
        freeScroll: true
        // prevNextButtons: false
      },
      visible: false
    };
  },
  props: {
    MovieList: {
      type: Array,
      default: function() {
        const x = JSON.parse(
          `{ "page": 1, "results": [ { "id": 287947, "video": false, "vote_count": 5217, "vote_average": 7, "title": "Shazam!", "release_date": "2019-03-29", "original_language": "en", "original_title": "Shazam!", "genre_ids": [ 28, 35, 14 ], "backdrop_path": "/OIGX2lm5tmlCKvZUghtwHzoxxO.jpg", "adult": false, "overview": "A boy is given the ability to become an adult superhero in times of need with a single magic word.", "poster_path": "/xnopI5Xtky18MPhK40cZAGAOVeV.jpg", "popularity": 35.271 }, { "id": 429617, "video": false, "vote_count": 7768, "vote_average": 7.6, "title": "Spider-Man: Far from Home", "release_date": "2019-06-28", "original_language": "en", "original_title": "Spider-Man: Far from Home", "genre_ids": [ 28, 12, 878 ], "backdrop_path": "/5myQbDzw3l8K9yofUXRJ4UTVgam.jpg", "adult": false, "overview": "Peter Parker and his friends go on a summer trip to Europe. However, they will hardly be able to rest - Peter will have to agree to help Nick Fury uncover the mystery of creatures that cause natural disasters and destruction throughout the continent.", "poster_path": "/4q2NNj4S5dG2RLF9CpXsej7yXl.jpg", "popularity": 59.564 }, { "adult": false, "backdrop_path": "/uK9uFbAwQ1s2JHKkJ5l0obPTcXI.jpg", "genre_ids": [ 35, 878 ], "id": 479455, "original_language": "en", "original_title": "Men in Black: International", "overview": "The Men in Black have always protected the Earth from the scum of the universe. In this new adventure, they tackle their biggest, most global threat to date: a mole in the Men in Black organization.", "poster_path": "/dPrUPFcgLfNbmDL8V69vcrTyEfb.jpg", "release_date": "2019-06-12", "title": "Men in Black: International", "video": false, "vote_average": 6, "vote_count": 2724, "popularity": 25.684 }, { "id": 299537, "video": false, "vote_count": 9647, "vote_average": 7, "title": "Captain Marvel", "release_date": "2019-03-06", "original_language": "en", "original_title": "Captain Marvel", "genre_ids": [ 28, 12, 878 ], "backdrop_path": "/w2PMyoyLU22YvrGK3smVM9fW1jj.jpg", "adult": false, "overview": "The story follows Carol Danvers as she becomes one of the universe’s most powerful heroes when Earth is caught in the middle of a galactic war between two alien races. Set in the 1990s, Captain Marvel is an all-new adventure from a previously unseen period in the history of the Marvel Cinematic Universe.", "poster_path": "/AtsgWhDnHTq68L0lLsUrCnM7TjG.jpg", "popularity": 42.968 }, { "id": 373571, "video": false, "vote_count": 2722, "vote_average": 6.3, "title": "Godzilla: King of the Monsters", "release_date": "2019-05-29", "original_language": "en", "original_title": "Godzilla: King of the Monsters", "genre_ids": [ 28, 878 ], "backdrop_path": "/jb6Ju38HmKX0bYHCmAxs8HyNeJ2.jpg", "adult": false, "overview": "Follows the heroic efforts of the crypto-zoological agency Monarch as its members face off against a battery of god-sized monsters, including the mighty Godzilla, who collides with Mothra, Rodan, and his ultimate nemesis, the three-headed King Ghidorah. When these ancient super-species - thought to be mere myths - rise again, they all vie for supremacy, leaving humanity's very existence hanging in the balance.", "poster_path": "/pU3bnutJU91u3b4IeRPQTOP8jhV.jpg", "popularity": 38.715 }, { "id": 456740, "video": false, "vote_count": 1900, "vote_average": 5.4, "title": "Hellboy", "release_date": "2019-04-10", "original_language": "en", "original_title": "Hellboy", "genre_ids": [ 28, 12, 14, 878 ], "backdrop_path": "/hMbP23EkGk6tjEjRZQXhnVAl5fW.jpg", "adult": false, "overview": "Hellboy comes to England, where he must defeat Nimue, Merlin's consort and the Blood Queen. But their battle will bring about the end of the world, a fate he desperately tries to turn away.", "poster_path": "/bk8LyaMqUtaQ9hUShuvFznQYQKR.jpg", "popularity": 32.295 }, { "id": 348350, "video": false, "vote_count": 5419, "vote_average": 6.6, "title": "Solo: A Star Wars Story", "release_date": "2018-05-15", "original_language": "en", "original_title": "Solo: A Star Wars Story", "genre_ids": [ 12, 878 ], "backdrop_path": "/7LZ0K4FsALrt7OeNIGOVLNuKQRU.jpg", "adult": false, "overview": "Through a series of daring escapades deep within a dark and dangerous criminal underworld, Han Solo meets his mighty future copilot Chewbacca and encounters the notorious gambler Lando Calrissian.", "poster_path": "/4oD6VEccFkorEBTEDXtpLAaz0Rl.jpg", "popularity": 31.403 }, { "id": 420817, "video": false, "vote_count": 6360, "vote_average": 7.1, "title": "Aladdin", "release_date": "2019-05-22", "original_language": "en", "original_title": "Aladdin", "genre_ids": [ 12, 35, 14, 10749, 10751 ], "backdrop_path": "/v4yVTbbl8dE1UP2dWu5CLyaXOku.jpg", "adult": false, "overview": "A kindhearted street urchin named Aladdin embarks on a magical adventure after finding a lamp that releases a wisecracking genie while a power-hungry Grand Vizier vies for the same lamp that has the power to make their deepest wishes come true.", "poster_path": "/ykUEbfpkf8d0w49pHh0AD2KrT52.jpg", "popularity": 46.318 }, { "id": 338952, "video": false, "vote_count": 6926, "vote_average": 6.9, "title": "Fantastic Beasts: The Crimes of Grindelwald", "release_date": "2018-11-14", "original_language": "en", "original_title": "Fantastic Beasts: The Crimes of Grindelwald", "genre_ids": [ 12, 14, 10751 ], "backdrop_path": "/qrtRKRzoNkf5vemO9tJ2Y4DrHxQ.jpg", "adult": false, "overview": "Gellert Grindelwald has escaped imprisonment and has begun gathering followers to his cause—elevating wizards above all non-magical beings. The only one capable of putting a stop to him is the wizard he once called his closest friend, Albus Dumbledore. However, Dumbledore will need to seek help from the wizard who had thwarted Grindelwald once before, his former student Newt Scamander, who agrees to help, unaware of the dangers that lie ahead. Lines are drawn as love and loyalty are tested, even among the truest friends and family, in an increasingly divided wizarding world.", "poster_path": "/fMMrl8fD9gRCFJvsx0SuFwkEOop.jpg", "popularity": 33.09 }, { "id": 181812, "video": false, "vote_count": 5169, "vote_average": 6.6, "title": "Star Wars: The Rise of Skywalker", "release_date": "2019-12-18", "original_language": "en", "original_title": "Star Wars: The Rise of Skywalker", "genre_ids": [ 28, 12, 878 ], "backdrop_path": "/SPkEiZGxq5aHWQ2Zw7AITwSEo2.jpg", "adult": false, "overview": "The surviving Resistance faces the First Order once again as the journey of Rey, Finn and Poe Dameron continues. With the power and knowledge of generations behind them, the final battle begins.", "poster_path": "/db32LaOibwEliAmSL2jjDF6oDdj.jpg", "popularity": 59.752 } ], "total_pages": 2, "total_results": 40 }`
        ).results;
        return x;
      }
    },
    listType: {
      type: String,
      default: "No Title"
    }
  },
  methods: {
    resolve_img_url: function(path) {
      return "https://image.tmdb.org/t/p/w342" + path;
    },
    onClick() {
      // console.log("More");
    }
  }
};
</script>
<style scoped>
.carousel {
  margin: 10px 20px;
}

.carousel-cell {
  height: 400px;
  width: 20%;
  margin: 0px;
  display: flex;
  justify-content: center;
}

.carousel-cell-image {
  max-height: 100%;
  max-width: 100%;
  margin: 0 auto;
  display: block;
  object-fit: cover;
}

.carousel-cell-image:hover {
  opacity: 0.7;
}

/* .carousel-cell-image.flickity-lazyloaded,
.carousel-cell-image.flickity-lazyerror {
  opacity: 1;
} */

.container {
  display: flex;
}

.content {
  width: 66%;
  margin: 5px;
  font-size: 15px;
}

.large-image {
  width: 33%;
  height: 100%;
  margin: 5px;
  object-fit: cover;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */
  .carousel {
    margin: 5px;
  }

  .carousel-cell {
    height: 100px;
    margin: 0px 5px;
  }
}
.card {
  margin: 2.5em;
}
.carousel-type-text {
  text-align: left;
  font-size: 2em;
  margin-bottom: 0%;
  margin-top: 1rem;
}
</style>
