<template>
	<div class="show">
		<div class="title" >
			<van-nav-bar
			
			  title="买家秀" 
			  left-arrow
			  @click-left="onClickLeft"
			  @click-right="onClickRight"
			>
			<van-icon name="search" slot="right" />
			</van-nav-bar>
		</div>
		<!-- <div class="banner">
			<van-tabs  >
			  <van-tab v-for="(item,index) in banerList.data" :title="item.name"></van-tab>
			</van-tabs>
		</div> -->
		
		<div class="user_show">
			
				
			
			<div class="zhan" v-for="(item,index) in showList.data">
				<a href="https://m.ataoju.com/show/item/id/210.html">
				<img :src="item.show_pic" alt="" class="showpic">
				<p>{{item.intro}}</p>
				</a>
				<van-divider />
				<div class="userpic"><img :src="item.userlogo" alt="" ><span>{{item.usernick}}</span></div>
			</div>
			<div class="zhan" v-for="(item,index) in show_2.data">
				<a href="https://m.ataoju.com/show/item/id/210.html">
				<img :src="item.show_pic" alt="" class="showpic">
				<p>{{item.intro}}</p>
				</a>
				<van-divider />
				<div class="userpic"><img :src="item.userlogo" alt="" ><span>{{item.usernick}}</span></div>
			</div>
		</div>
		
		
		
		
	</div>
</template>

<script>
	import {user_show} from '../datas.js'
	import {title_cate} from '../datas.js'
	import {show2} from '../datas.js'
	
	export default{
		data(){
			return{
				showList:null,
				show_2:null,
				banerList:null
			}
		},
		created() {
			this.showList=user_show
			this.show_2=show2
			this.banerList=title_cate
		},
		 methods: {
		    onClickLeft() {
		      this.$router.go(-1)
		    },
		    onClickRight() {
		      this.$router.push("/search")
		    }
		  }
		
	}
	
</script>

<style scoped="scoped" lang="less"> 
	.van-nav-bar{
		background:linear-gradient(to left,#FA4DBE 0,#FBAA58 100%)
	}
	.show{
		// display: flex;
		position:absolute;
		pos-top: 10px;
		width: 376px;
		// bottom: 150px;	
		// background: linear-gradient(to top,#FA4DBE 0,#FBAA58 100%)
			
		
	}
	.user_show{
		width: 376px;
		display: flex;
		flex-wrap: wrap;
		position: relative;
		padding-bottom: 60px;
		.zhan{
			border: 1px solid skyblue;
			border-radius: 5px;
			width: 172px;
			height: 296px;
			margin: 4px auto;
			padding: 5px ;
			img{
				width: 100%;
				border-radius: 10px;
			}
			.showpic{
				width: 100%;
				height: 188px;
			}
			p{
				height: 40px;
				font-size: 12px;
				overflow:hidden;
			}
			.userpic{
				height: 30px;
				img{
					float: left;
					border-radius: 10px;
					width: 20px;
					height: 20px;
				}
				span{
					font-size: 12px;
					margin-right: 10px;
				}
			}
		}
	}
</style>
