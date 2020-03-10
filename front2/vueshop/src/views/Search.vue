<template>
	<div class="search">
		<div class="title_search">
			<div class="box1"  @click="return_up">
				<img src="../assets/return.png" alt="" style="width: 100%;">
			</div>
			<div class="box2">
				
				<van-search
				background="linear-gradient(to left,#FA4DBE 0,#FBAA58 100%)"
			  v-model="value"
			  placeholder="请输入搜索关键词"
			  shape="round"
			  @search="onSearch" 
			/>
			</div>
			<div class="box3" @click="onSearch">
				<p>搜索</p>
			</div>
			
		</div>
		
		<div>
			<van-divider>热门搜索</van-divider>
		<div class="middles" style="display: flex;flex-wrap: wrap;" >
			
			<div style="margin: 10px auto;" v-for="(item,index) in tabs">
				<van-tag round >{{item}}</van-tag>
			</div>
		</div>
		<van-divider>。。。</van-divider>
		<div v-if="falg" style="text-align: center;">
	
			{{value}}
		</div>
		</div>
	</div>
</template>

<script>
	export default{
		data(){
			return{
				value:null,
				falg:false,
				tabs:[
					"电风扇","电风扇","电风扇","电风扇","电风扇","电风扇","电风扇",
				]
			}
		},
		methods:{
			onSearch(){
				// this.$router.push("/")
				this.falg=true
			},
			return_up(){
				this.$router.go(-1)
			}
		}
	}
</script>

<style scoped="scoped" lang="less">
	
		
	.title_search{
		display: flex;
		flex-wrap: wrap;
		background: linear-gradient(to left,#FA4DBE 40%,#FBAA58 10%);
		.box1{
			// background-color: gray;
			border-radius: 50%; 
			width: 30px;
			height: 30px;
			// margin: 0 ;
			padding: 5px;
			margin-top: 5px;
		}
		.box3{
			margin-top: 10px;
			width: 50px;
			height: 30px;
			background-color: darkorange;
			border-radius: 50% ;
			p{
				margin-top: 5px;
			}
		}
	}

		
	
</style>
