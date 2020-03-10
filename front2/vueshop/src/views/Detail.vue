<template>
	<div class="detail" style="padding-bottom: 50px;">
		<div class="box1" @click="ret" >
			<img src="../assets/return.png" alt="" style="width: 100%;">
		</div>
		<div>
			<van-goods-action>
			  <van-goods-action-icon icon="chat-o" text="客服" @click="onClickIcon" />
			  <van-goods-action-icon icon="cart-o" text="购物车" @click="onClickIconto" />
			  <van-goods-action-button type="warning" text="加入购物车" @click="onClickButton" />
			</van-goods-action>
		</div>
		<div class="sp1">
			<div class="img_1">
				<img src="https://img.alicdn.com/i4/848001452/O1CN01jVZzqZ1Mb3am75lZA_!!848001452.jpg" alt="">
			</div>		
		</div>
		<div class="msg">
			<p>香港梵蜜琳神仙贵妇膏正品8g 明星美颜面霜抖音网红推荐特价买它</p>
		</div>
		<div>
			<img src="https://img.alicdn.com/imgextra/i3/848001452/O1CN01xjsg721Mb3fOAEPP5_!!848001452.jpg" style="width: 100%;height: 100%;" alt="">
		</div>
		<div>
			<img src="https://img.alicdn.com/imgextra/i1/848001452/O1CN01anRAGC1Mb3ab2BOQI_!!848001452.jpg" style="width: 100%;height: 100%;" alt="">
		</div>
		
		<div class="shul" style="display: flex;flex-wrap: wrap;">
			<p>商品数量：</p>
			<p style="padding-left: 180px;"><van-stepper v-model="value" /></p>
		</div>
		
		
		
		
	</div>
</template>

<script>
	export default {
		data(){
			return{
				value: 1
			}
		},
	  methods: {
		  ret(){
			this.$router.go(-1)  
		  },
	    onClickIcon() {
	      this.$toast('点击图标');
	    },
	    onClickButton() {
	      this.$toast('点击按钮');
	    },
		onClickIconto(){
			this.$router.push("/cart")
		}
	  }
	}
	
</script>

<style scoped="scoped" lang="less">
	
	.box1{
		float: left;
		// background-color: gray;
		border-radius: 50%; 
		width: 30px;
		height: 30px;
		// margin: 0 ;
		padding: 5px;
		margin-top: 5px;
	}
	.van-tabbar--fixed{
		position: none;
	}
	.van-tabbar{
		display: none;
	}
	.sp1{

		background: linear-gradient(to top,#e5e5e5 0,#fe3a33 100%);
	
		.img_1{
			width: 220px;
			height: 180px;
			padding-left: 96px;
		
			img{
				width: 100%;
				height: 100%;
			}
		}
		
	}
</style>
