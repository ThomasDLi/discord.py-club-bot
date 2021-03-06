@client.command(aliases=['join'])
async def joinclub(ctx, club):
	ef = "club: {}".format(club)
	role = discord.utils.get(ctx.author.guild.roles, name=ef)
	await ctx.author.add_roles(role)
	await ctx.send(":white_check_mark: Joined the {} club".format(club))


@client.command(aliases=['leave'])
async def leaveclub(ctx, club):
	ef = "club: {}".format(club)
	role = discord.utils.get(ctx.author.guild.roles, name=ef)
	await ctx.author.remove_roles(role)
	await ctx.send(":white_check_mark: Left the {} club".format(club))


@client.command()
async def pingclub(ctx, club):
	ef = "club: {}".format(club)
	role = discord.utils.get(ctx.author.guild.roles, name=ef)
	await ctx.send("{}, {} members".format(role.mention, len(role.members)))

@commands.has_permissions(manage_guild=True)
@client.command()
async def createclub(ctx, fa, *yes):
  channel = client.get_channel(123456789)#               <--- REPLACE 123456789 WITH CHANNEL ID
  await ctx.guild.create_role(name="club: {}".format(fa))
  await channel.send("> **CLUB: {}**\n> {}".format(fa.upper(), " ".join(yes)))
