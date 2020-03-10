<template>
	<div>
		

	<div class="title" >
		<van-nav-bar
		
		  title="分类导航" 
		  left-arrow
		  @click-left="onClickLeft"
		  @click-right="onClickRight"
		>
		<van-icon name="search" slot="right" />
		</van-nav-bar>
	</div>
	<div class="daoh" style="display: flex;flex-wrap: wrap;margin: 5px;">
		<div class="tos" v-for="(item4,index) in toPi.data" >
			<div class="k" style="width: 72px;height: 72px; margin: 8px;" >
				<!-- <a href="https://m.ataoju.com/index/cate/cid/1.html"> -->
				<img :src="item4.icon" alt="" style="width: 100%;height: 100%;">
				<span style="font-size: 12px;">{{item4.name}}</span>
				<!-- </a> -->
			</div>
		</div>
	</div>
		</div>
</template>

<script>
	import {to_pi} from'../datas.js'
	export default{
		data(){
			return{
				toPi:null
			}
		},
		methods: {
		   onClickLeft() {
		     this.$router.go(-1)
		   },
		   onClickRight() {
		     this.$router.push("/search")
		   }
		 },
		
		created() {
			this.toPi=to_pi
		}
	}
</script>

<style>
</style>
