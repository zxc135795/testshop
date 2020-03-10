<template>
	<div class="category">
		<div @click="search">
			<van-search  placeholder="请输入搜索关键词" v-model="value" background="linear-gradient(to left,#FA4DBE 0,#FBAA58 100%)" />
		</div>
		
		
		<div class="left_baner">
			<div class="left">
				<van-sidebar v-model="activeKey">
				  <van-sidebar-item v-for="(item,index) in fenList.data"   :title="item.name" />
				</van-sidebar>
			</div>
			
			<div class="right_shop">
				<div class="items" v-for="(item,index) in fenList.data" v-if="activeKey==index">
					<div class="shop_show" v-for="(item1,index) in item.sub_class">
						<router-link to="/detail">
							<div>
								<img :src="item1.icon" alt="">
							</div>
							<span>{{item1.name}}</span>
						</router-link>
						
					</div>
					
				</div>
			
		</div>
		</div>	
	</div>
</template>

<script>
import {fen_list} from '../datas.js'
	
	
	export default {
	  data() {
	    return {
			value:null,
	      activeKey: 0,
		  fenList:null
	    };
	  },
	  created() {
	  	this.fenList=fen_list
	  },
	  methods:{
		  search(){
			  this.$router.push("/search")
		  }
	  }
	}
</script>

<style scoped="scoped" lang="less">
	.left_baner{
		display: flex;
		position: absolute;
		left:0;
		top:55px;
		right:0;
		bottom: 50px;
		.left{
			overflow-y: auto;
			width: 25%;
			.van-sidebar-item--select{
				border:none;
				color: #fb7d34;
				font-size: 16px;
			}
	}
	}
	.right_shop{
		overflow-y: auto;
		width: 75%;
		.items{
			display: flex;
			flex-wrap: wrap;
		}
		.shop_show{
			display: flex;
			flex-wrap: wrap;
			flex-direction: column;
			width: 87px;
			height: 80px;
			margin: 10px 0 15px;
			align-items: center;
			img{
				width: 52px;
				height: 52px;
			}
			span{
				font-size: 12px;
			}
		}
	}

</style>
