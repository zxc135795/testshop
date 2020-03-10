<template>
  <div class="mine" >
  
	  <div v-if="userinfo!=null" style="display: flex;flex-wrap: wrap;background:linear-gradient(to left,#FA4DBE 0,#FBAA58 100%)">
	  	<div style="display: flex;flex-wrap: wrap;" >
			<div style="border-radius: 50px;width: 50px;height: 50px;border:1px solid; margin: 50px;" >
				<img src="https://m.ataoju.com/static/wap/images/yaoqing.svg" alt="" style="width: 100%;">
			</div>
			<div style="margin-top: 50px;width: 50px;height: 50px;overflow: hidden;">
				<p>{{userinfo}}</p>
			</div>
		</div>
		
		
		<!-- <div  @click="loginout" style="background-color: red; border: 1px red solid; width: 64px;height: 24px;margin-left: 150px;margin-top: 12px;border-radius: 20%;">
			<span style="color:  snow;">注销</span>
		</div> -->
	  	
	  	<br>
	  	<br>
	  	<br>
		<div style="background-color: aliceblue;width: 100%;margin-bottom: 50px; ">
			<div style="background-color: aliceblue;width: 100%; " v-for="item in 3">
				<div style="width: 100%; float: left; margin-bottom: 10px; background-color: white;">
					<p  >
						<img src="https://m.ataoju.com/static/wap/images/yaoqing.svg" alt="">
						<span style="padding-left: 10px;">邀请新人</span>
						<img src="../assets/dayu.png" alt="" style="width: 24px;height: 24px; margin-left: 240px;">
					</p>
					<p  >
						<img src="https://m.ataoju.com/static/wap/images/wode_icon_like.svg" alt="">
						<span style="padding-left: 10px;">我的收藏</span>
						<img src="../assets/dayu.png" alt="" style="width: 24px;height: 24px; margin-left: 240px;">
					</p>
					<p  >
						<img src="https://m.ataoju.com/static/wap/images/wode_icon_history.svg" alt="">
						<span style="padding-left: 10px;">我的足迹</span>
						<img src="../assets/dayu.png" alt="" style="width: 24px;height: 24px; margin-left: 240px;">
					</p>
				</div>			
			</div>
		</div> 	
		<div style="margin-bottom: 50px;margin-top: -50px;width: 374px;margin-left: 1px;">
			<van-button type="primary"    @click="loginout" size="large" plain hairline color="red"><b>注销</b></van-button>
		</div>
	  	
		</div>
	  
	  
	  
	  
	<div class="box_1" v-else>
		<van-tabs v-model="active" background="linear-gradient(to left,#FA4DBE 0,#FBAA58 100%)"
		>
		
		<van-tab title="登录"  >
		<div class="login">
			<p> 登录 用户 </p>
			
			<van-cell-group>
			  <van-field
				v-model="loginusername"
				required
				clearable
				label="用户名"
				placeholder="请输入用户名/邮箱"
			  />
			
			  <van-field
				v-model="loginpassword"
				type="password"
				label="密码"
				placeholder="请输入密码"
				required
			  />
			</van-cell-group>
			
			<van-button type="primary" @click="login" >登录</van-button>
		</div>
		 </van-tab>
		 <van-tab title="注册">
		<div class="regist">
			<p> 注册 用户 </p>
			
			<van-cell-group>
			  <van-field
				v-model="username"
				required
				clearable
				label="用户名"
				placeholder="请输入用户名"
			  />
			
			  <van-field
				v-model="password"
				type="password"
				label="密码"
				placeholder="请输入密码"
				required
			  />
			  
			  <van-field
				v-model="password2"
				type="password"
				label="重复密码"
				placeholder="请再次输入密码"
				required
			  />
			  
			  <van-field
				v-model="email"
				type="email"
				label="邮箱"
				placeholder="请输入邮箱"
				required
			  />
			</van-cell-group>
			
			<van-button type="primary" @click="regist" >注册</van-button>
		</div>
		</van-tab>
		</van-tabs>
		
	</div>
  </div>
</template>
<script>
	
	export default{
		data(){
			return{
				active:0,
				username:"py191101",
				password:"123456789",
				password2:"123456789",
				email:"496575233@qq.com",
				loginusername:"py191101",
				loginpassword:"123456789",
				userinfo:null,
				data:{
					Name:"ggd",
					Time:"hfsef",
					Honor:"hgdrf"
					
					}
				
			}
		},
		created() {
			this.initUser();
		},
		methods:{
			initUser(){
				this.userinfo = localStorage.getItem("userinfo")
			},
		
			loginout(){
				this.$toast("退出成功");
				this.userinfo=null;
				localStorage.removeItem("userinfo")
				
			},
			login(){
				if(this.loginusername.length<=0||this.loginpassword.length<=0){
					this.$toast("必填项目不能为空");
				}else{
					this.$toast("登陆成功")
				this.data.Name=this.loginusername
				// this.userinfo = this.data
				
				localStorage.setItem("userinfo",this.data.Name)
				if(this.$route.query.redirect){
					this.$router.push(this.$route.query.redirect);
					
				}
				this.initUser();
				
				
				}
				
			},
			regist(){
				
				if(this.email.length<=0||this.username.length<=0||this.password.length<=0||this.password2.length<=0){
					this.$toast("必填项目不能为空");
				}
				else if(this.password!=this.password2)
				{
					this.$toast("密码必须一致");
				}
				else{
					
					this.$toast("注册成功");
					this.active=0
				}
			}
		}
	}
</script>
<style>

</style>
