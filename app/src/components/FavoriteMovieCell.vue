<template>
  <li>
    <img :src="item.img" />
    <br />
    <div>
      <a class="title">{{ item.title }}</a>
      <div class="d-flex items-center area muted">
        <p class="year">{{ item.release_year }}</p>
        <p class="separator genres">{{ genres }}</p>
      </div>
      <p class="area plot">{{ item.overview }}</p>
      <div class="d-flex items-center area">
        <p class="rating" title="Rating" v-show="item.popularity">
          <span class="rating--star"></span>
          {{ item.rating }}
        </p>
      </div>
    </div>
  </li>
</template>

