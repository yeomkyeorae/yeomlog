<template>
	<div>
		<div class="font-sans antialiased">
			<nav class="flex items-center justify-between flex-wrap bg-pink-400 p-3">
				<div class="flex items-center flex-no-shrink text-white mr-6">
					<span class="font-semibold text-l tracking-tight">
						Curriculum Vitae
					</span>
				</div>
				<div class="block sm:hidden">
					<button @click="toggle"
						class="flex items-center px-3 py-2 border rounded text-teal-lighter border-teal-light hover:text-white hover:border-white">
						<svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
							<title>Menu</title>
							<path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
						</svg>
					</button>
				</div>
				<div :class="open ? 'block': 'hidden'" class="w-full flex-grow sm:flex sm:items-center sm:w-auto">
					<div class="text-sm sm:flex-grow">
						<router-link :to="profile.path"
							class="no-underline block mt-4 sm:inline-block sm:mt-0 text-white hover:text-white mr-4">
							<span class="text-white">
								<i class="material-icons">{{ profile.icon }}</i>Profile
							</span>
						</router-link>
						<router-link :to="account.path"
							class="no-underline block mt-4 sm:inline-block sm:mt-0 text-white hover:text-white mr-4">
							<span class="text-white">
								<i class="material-icons">{{ account.icon }}</i>Accounts
							</span>
						</router-link>
						<router-link :to="certificate.path"
							class="no-underline block mt-4 sm:inline-block sm:mt-0 text-white hover:text-white mr-4">
							<span class="text-white">
								<i class="material-icons">{{ certificate.icon }}</i>Certificates
							</span>
						</router-link>
						<router-link :to="interest.path"
							class="no-underline block mt-4 sm:inline-block sm:mt-0 text-white hover:text-white mr-4">
							<span class="text-white">
								<i class="material-icons">{{ interest.icon }}</i>Interests
							</span>
						</router-link>
						<router-link :to="skill.path"
							class="no-underline block mt-4 sm:inline-block sm:mt-0 text-white hover:text-white mr-4">
							<span class="text-white">
								<i class="material-icons">{{ skill.icon }}</i>Skills
							</span>
						</router-link>
						<router-link :to="project.path"
							class="no-underline block mt-4 sm:inline-block sm:mt-0 text-white hover:text-white mr-4">
							<span class="text-white">
								<i class="material-icons">{{ project.icon }}</i>Projects
							</span>
						</router-link>
					</div>
				</div>
			</nav>
		</div>
		<router-view />
	</div>
</template>

<script>
	export default {
		name: 'Cv',
		components: {

		},
		data() {
			return {
				open: false,
				profile: {
					path: '/cv/profile',
					icon: 'assignment_ind'
				},
				account: {
					path: '/cv/account',
					icon: 'person_pin'
				},
				certificate: {
					path: '/cv/certificate',
					icon: 'all_inbox'
				},
				interest: {
					path: '/cv/interest',
					icon: 'favorite'
				},
				skill: {
					path: '/cv/skill',
					icon: 'extension'
				},
				project: {
					path: '/cv/project',
					icon: 'dashboard'
				},
			}
		},
		methods: {
			toggle() {
				this.open = !this.open
			}
		}
	}
</script>
<style>
	.cv {
		text-align: left;
	}
</style>