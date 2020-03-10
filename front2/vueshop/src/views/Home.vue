<template>
  <div class="home">
	<div class="search">
		<div class="header">
			<div class="left">
				<img src="https://m.ataoju.com/static/wap/images/sigin.gif" alt="">
			</div>
			<div class="middle" >
					 <!-- <van-search :disabled="true" placeholder="请输入搜索关键词" v-model="searchValue" /> -->
				<van-search placeholder="请输入搜索关键词" v-model="value" shape="round" background="#fe3a33" :disabled="true" @click="to_search" />
			</div>
			<div class="right" @click="cart">
				<van-icon name="shopping-cart"  size="32px" color="#fff" />
			</div>
			<div class="down" @click="down" >
				<img src="../assets/xia.png" alt="" >
			</div>
		</div>	
	</div>
	<div class="box">
		<div class="cate" >
			<van-tabs background="#fe3a33" >
			  <van-tab v-for="(item,index) in baner.data" :title="item.name" to="/category" >
				 <!-- <Daoh :items="item"></Daoh> --> 
			  </van-tab>
			</van-tabs>
		</div>

		<div class="lun">
			<van-swipe :autoplay="3000" indicator-color="#fe3a33"  >
			  <van-swipe-item v-for="(item,index) in headCarousel.data.config" >
				  <img :src="item.pic" alt="">
			  </van-swipe-item>
			</van-swipe>
		</div >
			
		<div class="dao">
			<div class="dh" v-for="(item,index) in headDh.data.config.data">
				<a href="https://m.ataoju.com/renqi.html">
				<img :src="item.address" alt="" >
				<span style="color: aliceblue;">{{item.name}}</span></a>
			</div>
		</div>
		
		<div class="fount">
			<p ><van-divider ><h3>发现好货</h3></van-divider></p>
			<van-notice-bar
			
			background="#f3c1bd"
			  left-icon="volume-o"
			>
			 【艾绫】智能温控自发热男女马甲
			</van-notice-bar>
			<div class="fount_shop" >
				<div class="box1" v-for="(item,index) in fountShop.data.data" :items="item.id">
					<router-link to="/detail">
						<div class="box2"  >
							<img :src="item.pic" alt="">
							<p>{{item.title}}</p>
							<div>
								<span>
									<span style="margin-right: 10px;background-color: orangered;border-radius: 10px;">{{item.quan}}元券</span>
									<span style="margin-left: 10px;margin: 0;border-radius: 5px; box-sizing: border-box; border: 1px red solid; color: red;font-size: 14px;">最高返{{item.commission}}</span>	
								</span>
							
							</div>
							<div>
								<p style="color: red;">券后￥{{item.coupon_price}}</p>
							</div>
						</div>
					</router-link>				
				</div>			
			</div>
		</div>
	</div>
  </div>
</template>
<style scoped="scoped" lang="less">
	.header{
		display: flex;
		line-height: 40px;
		height: 40px;
		.left{
			margin: 0 10px;
			img{
				height: 32px;
				vertical-align: middle;
			}
		}
		.middle{
			flex: 1;
			background:#fe3a33;
			.van-search{
				padding-top:8px ;
			}
		}
		.right{
			margin:  10px ;
			img{
				height: 26px;
				vertical-align: middle;
			}
		}
		.down{
			margin:5px ;
			img{
				height: 26px;
				vertical-align: middle;
			}
		}
	}
	.home{
		margin: 0 auto;
		background: linear-gradient(to top,#e5e5e5 90%,#fe3a33 100%)
		}
	.search{
		// background-color: #fe3a33;
		display: flex;
		line-height: 44px;
		height: 44px;
		.heds{
			flex: 1;
			.van-search{
				padding-top:5px ;
			}
		}
	}
	.cate{
		width: 375px;
		margin: 0 auto;
		img{
			height: 26px;
			vertical-align: middle;
		}
		
		.lun{
			width: 376px;
			
		}
	
	}
	.dao{
		width: 376px;height: 160px;
		// position: absolute;
		top: 300px;
		display: flex;
		flex-wrap: wrap;
		align-items: auto;
	
		.dh{
			// position: relative;
			text-align: center;
			width: 50px;
			height: 50px;
			padding: 5px 6px 7px 13px;
			margin: 0 auto ;
			img{
				width: 100%;
			}
			span{
				font-size: 12px;
				
			}
		}
	}
	
	.fount{
		// position: relative;
		width: 376px;
		
		.fount_shop{
			display: flex;
			flex-wrap: wrap;
			width: 376px;
			margin: 0 auto;
			padding-bottom: 50px;
			
			.box1{
				display: flex;
				flex-wrap: wrap;
				width: 160px;
				padding-left: 20px;
			
				.box2{
					font-size: 12px;
					background-color: white;
					display: flex;
					flex-wrap: wrap;
					border-radius: 10px;
					padding: 5px;
					margin: 5px auto;
					
					div{
						font-size: 16px;
						border-radius: 10px;
						// padding-left: 10px;
					}
				}
				img{
					width: 100%;
					border-radius: 10px;
				}
			}
			
			
		}
		
	}
</style>


<script>
// @ is an alias to /src
import Daoh from '@/components/Daoh.vue'
import {s_t_lun} from '../datas.js'
import {s_f} from '../datas.js'
import {s_fount} from '../datas.js'

import {you_hui} from '../datas.js'
import {title_cate} from '../datas.js'



export default {
  name: 'home',
  components: {
    // HelloWorld
	Daoh
  },
  props:["itemid"],
  data(){
	  return{
		  value:'',
		  headCarousel:null,
		  headDh:null,
		  fountShop:null,
		  baner:null,
		  
	  }
  },
  created() {
  	this.headCarousel=s_t_lun
	this.headDh=s_f
	this.fountShop=s_fount
	this.baner=title_cate
  },
  methods:{
	  togo(){
		  this.$router.push("/daoh")
	  },
	  to_search(){
		  this.$router.push("/search")
	  },
	  cart(){
		  this.$router.push("/cart")
	  },
	  down(){
		  this.$router.push("/search")
	  },
	  todao(item){
		  this.$router.push("/daoh")
	  }
	  
  },
  props:["items"]
}
</script>
