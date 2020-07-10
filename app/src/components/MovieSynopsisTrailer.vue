<template>
  <div class="card">
    <div class="trailer-body" style="background: #1e1d1d">
      <div class="has-text-centered">
        <div class="columns">
          <div class="column vertical-align">
            <iframe
              allowfullscreen
              frameborder="0"
              height="376"
              src="https://www.youtube.com/embed/QWbMckU3AOQ?autoplay=1&modestbranding=1"
              style="width: 100%; min-width: 536px"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieSynopsisTrailer"
};
</script>

<style scoped>
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
.card {
  margin: 1.5em;
}
</style>