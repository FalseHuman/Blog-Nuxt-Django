<template>
<div>
  <p>Всего статей: {{articles.length}}</p>
  <template v-for="article in articles">
    <div :key="article.id">
    <li><nuxt-link class="black" :to="`articles/${article.id}`">{{article.article_title}};</nuxt-link></li>
    </div> 
  </template>
</div>
</template>
<script>
export default {
  head() {
    return {
      title: "Список статей"
    };
  },
    async asyncData({ $axios, params }) {
    try {
      let articles = await $axios.$get(`/articles/`);
      return { articles  };
    } catch (e) {
      return { articles: [] };
    }
  },
  data() {
    return {
      articles : [],
    };
  },
};
</script>
<style scoped>
.black{
  color: black;
}
</style>
