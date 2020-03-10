<template>
	<div class="cart">
		<div class="tit">
			<van-nav-bar
			
			  title="购物车" 
			  left-arrow
			  @click-left="onClickLeft"
			  @click-right="onClickRight"
			>
			<van-icon name="search" slot="right" />
			</van-nav-bar>
		</div>
		<div style="padding-bottom: 120px;" class="shops">
			<div  v-for="(item ,index) in shopList" :key="index">
				<van-card
				  
				  :price="item.price"
				  :desc="item.ms"
				  :title="item.name"
				  thumb="https://img.yzcdn.cn/vant/t-thirt.jpg"
				>
				  <div slot="footer">
				    <van-button size="mini" @click="def(index)">-</van-button>
					<span>{{item.num}}</span>
				    <van-button size="mini" @click="add(index)">+</van-button>
				  </div>
				</van-card>
			</div>
		</div>
		
	</div>
	
	
	
</template>

<script>
	export default{
		data(){
			return{
				num:1,
				shopList:[
					{num:1,name:"商品1",ms:"0000000000",price:"66"},
					{num:1,name:"商品1",ms:"0000000000",price:"66"},
					{num:1,name:"商品1",ms:"0000000000",price:"66"},
					{num:1,name:"商品1",ms:"0000000000",price:"66"},
					{num:1,name:"商品1",ms:"0000000000",price:"66"},
				]
			}
		},
		methods:{
			onClickLeft(){
				this.$router.go(-1)
			},
			onClickRight(){
				this.$router.push("/search")
			},
			def(index){
				this.shopList[index].num--
			},
			add(index){
				this.shopList[index].num++
			}
		}
	}
</script>

<style scoped="scoped" lang="less">
	.van-tabbar--fixed{
		position: none;
	}
	.van-tabbar{
		display: none;
	}
	.van-nav-bar{
		background:linear-gradient(to left,#FA4DBE 0,#FBAA58 100%)
	}
	.cart{
		// position: fixed;
		display: flex;
		flex-wrap: wrap;
		// position: fixed;
		// margin-top: 80px;
		flex-direction: column;
		width: 376px;
		// height: 100%;
		// padding-bottom: 50px;
	}
	.tit{
		position: relative;
		top: 0px;
		position: fixed;
		width: 376px;
		margin-top: 0px;
		// flex: 0;
		
		
		
		
	}
	.shops{
		position: absolute;
		// position: sticky;
		top: 50px;
		left: 0;
		right: 0;
		bottom: 50px;
		flex: 1;
		overflow-y: scroll;
	}
	

</style>
