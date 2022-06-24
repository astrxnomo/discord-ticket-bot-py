import discord
import datetime
from discord.ext import commands
from discord_components import Button, Select, SelectOption, ComponentsBot, interaction
from discord_components.component import ButtonStyle

bot = ComponentsBot("tb!", help_command=None)

embed_color = 0xfcd005
id_category = 987014930043633694
id_channel_ticket_logs = 987015105743032330
id_staff_role = 987017871102197790


@bot.event
async def on_ready():
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'{members} members' #Bot status
    ))
    print('Ready to support ✅')


@bot.command()
@commands.has_permissions(administrator=True)
async def ticket(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Soporte', description='Este canal te servirá para resolver tus dudas, inquietudes, reclamos y muchos otros temas relacionados con el servidor.\n\n> ¿Necesitas soporte?, presiona el boton `🔧 Solicitar soporte`\n\n> A continuacion tendrás un menu donde seleccionaras el tema de tu necesidad, se abrirá un ticket y esperamos aclarar tus dudas, problemas y lo que necesites.', color=embed_color)
    embed.set_image(url='https://i.imgur.com/P7S0YSd.jpeg')
    await ctx.send(
        embed = embed,
        components = [
            Button(
                custom_id = 'soporte',
                label = "Solicitar soporte",
                style = ButtonStyle.green,
                emoji ='🔧')
        ]
    )

@bot.event
async def on_button_click(interaction):

    canal = interaction.channel
    canal_logs = interaction.guild.get_channel(id_channel_ticket_logs)

    if interaction.component.custom_id == "soporte":
        await interaction.send(
            "`Presiona click para desplegar el menu` ⤵️",
            components = [
                Select(
                    placeholder = "¿En qué te podemos ayudar?",
                    options = [
                        SelectOption(label="FAQ", value="FAQ", description='Para resolver tus dudas respecto al servidor.', emoji='❔'),
                        SelectOption(label="Reportes", value="reportes", description='Para reportar usuarios por flood, spam o toxicidad.', emoji='🚫'),
                        SelectOption(label="Desbaneos", value="desbaneos", description='Para saber como ser desbaneado del servidor.', emoji='📄'),
                        SelectOption(label="Regalos", value="regalar", description='Para regalar roles, cuentas o codigos.', emoji='🎁'),
                        SelectOption(label="Comprar Patrocinador", value="patrocinador", description='Para tener asesoria en la compra del rol Patrocinador', emoji='🛒')
                    ],
                    custom_id = "menu")])

    elif interaction.component.custom_id == 'cerrar_ticket':
        embed_cerrar_ticket = discord.Embed(description=f"⚠️ ¿Seguro que quieres cerrar el ticket?", color=embed_color)
        await canal.send(interaction.author.mention, embed=embed_cerrar_ticket, 
                        components = [[
                        Button(custom_id = 'cerrar_si', label = "Sí", style = ButtonStyle.green),
                        Button(custom_id = 'cerrar_no', label = "No", style = ButtonStyle.red)]])
    
    elif interaction.component.custom_id == 'llamar_staff':

        embed_llamar_staff = discord.Embed(description=f"🔔 {interaction.author.mention} ha llamado al staff.", color=embed_color)
        await canal.send(f'<@&{id_staff_role}>', embed=embed_llamar_staff, delete_after= 20)


    elif interaction.component.custom_id == 'cerrar_si':

        await canal.delete()
        embed_logs = discord.Embed(title="Tickets Soporte", description=f"", timestamp = datetime.datetime.utcnow(), color=embed_color)
        embed_logs.add_field(name="Ticket", value=f"{canal.name}", inline=True)
        embed_logs.add_field(name="Cerrado por", value=f"{interaction.author.mention}", inline=False)
        embed_logs.set_thumbnail(url=interaction.author.avatar_url)
        await canal_logs.send(embed=embed_logs)

    elif interaction.component.custom_id == 'cerrar_no':

        await interaction.message.delete()

    elif interaction.component.custom_id == 'ya_pague':

        embed_logs = discord.Embed(title="¿Ya hiciste el pago? Ahora sigue estos pasos:", color=embed_color)
        embed_logs.add_field(name="Paso 1", value='Enviar captura de pantalla donde sea vea la transaccion completa.', inline=False)
        embed_logs.add_field(name="Paso 2", value=f"Cuando hayas completado el **Paso 1** presiona el botón `✅Completado`", inline=False)
        embed_logs.add_field(name="Paso 3", value=f"Espera un momento mientras el staff encargado confirma tu pago.", inline=False)
        embed_logs.add_field(name="Paso 4", value=f"Cuando se haya confirmado el pago te pondremos el rol y ya puedes disfrutarlo.", inline=False)
        await canal.send(interaction.author.mention, embed=embed_logs, components = [
                        Button(custom_id = 'llamar_staff', label = "Completado", style = ButtonStyle.green, emoji='✅')])

    elif interaction.component.custom_id == 'apoyar_pibarbot':
        await interaction.send("Revisa tus mensajes privados 🥳")
        channel = await interaction.user.create_dm()
        
        embed = discord.Embed(title = '⭐ | Apoya a Pibarbot', description = 'Puedes apoyar el bot comprando rol **Patrocinador**.\n\n**¿No sabes como comprarlo?** Conoce como comprar el rol en el siguiente canal: <#845508811699912704>\n\n> Con el dinero recogido podremos pagar lo que cuesta mantenerlo cada mes y seguir añadiendole nuevas funciones.', color=embed_color)
        embed.set_footer(text="© Los Pibardos")
        embed.set_image(url = 'https://i.imgur.com/ezKeB0O.png')
        await channel.send(embed = embed)

@bot.event
async def on_select_option(interaction):
    if interaction.component.custom_id == "menu":

        guild = interaction.guild
        category = discord.utils.get(interaction.guild.categories, id = id_category)
        rol_staff = discord.utils.get(interaction.guild.roles, id = id_staff_role)


        if interaction.values[0] == 'FAQ':
            canal = await guild.create_text_channel(name=f'❔┃{interaction.author.name}-ticket', category=category)
            await canal.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await canal.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)
            await canal.set_permissions(rol_staff,
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True,
                                                manage_messages=True)
                                                
            await interaction.send(f'> Se creó el canal {canal.mention} para resolver tus dudas 🕵️', delete_after= 3)

            embed_faq_inicio = discord.Embed(title=f'FAQ - ¡Hola {interaction.author.name}!', description='En este ticket tenemos respuesta a las dudas más frecuentes sobre el servidor.\n\nSi no encuentras una respuesta a tu duda o problema presiona el boton de `🔔 Llamar staff` para hablar personalmente con el staff del servidor y resolver tus dudas.', color=embed_color)
            embed_faq_inicio.set_thumbnail(url=interaction.author.avatar_url)
            embed_faq = discord.Embed(title='Preguntas Frecuentes - FAQ', color=embed_color)
            embed_faq.add_field(name= '¿Cuando hay postulaciones a Staff?', value= 'En este momento no hay postulaciones para ser staff, deberás estar pendiente al canal de <#845494172672983040> donde avisaremos cuando las hayan.' )

            await canal.send(interaction.author.mention, embed=embed_faq_inicio)
            await canal.send(embed=embed_faq, components = [[
                    Button(custom_id = 'cerrar_ticket', label = "Cerrar ticket", style = ButtonStyle.red, emoji ='🔐'),
                    Button(custom_id = 'llamar_staff', label = "Llamar staff", style = ButtonStyle.blue, emoji ='🔔')]])

        if interaction.values[0] == 'reportes':
            canal = await guild.create_text_channel(name=f'🚫┃{interaction.author.name}-ticket', category=category)
            await canal.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await canal.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)
            await canal.set_permissions(rol_staff,
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True,
                                                manage_messages=True)

            await interaction.send(f'> Se creó el canal {canal.mention} para que hagas tu reporte 🚫')

            embed_reportes = discord.Embed(title=f'Reportes - ¡Hola {interaction.author.name}!', description='¿Quieres reportar a un usuario del servidor?, sigue estos pasos:',  color=embed_color)
            embed_reportes.add_field(name='Paso 1', value='Leer las advertencias.', inline=False)
            embed_reportes.add_field(name='Paso 2', value='Escribe la **ID del usuario**. (Si no sabes mira como hacerlo [aquí](https://support.discord.com/hc/es/articles/206346498--D%C3%B3nde-puedo-encontrar-mi-ID-de-usuario-servidor-mensaje-))', inline=False)
            embed_reportes.add_field(name='Paso 3', value='Escribe la **razón** por la que estás reportando este usuario.', inline=False)
            embed_reportes.add_field(name='Paso 4', value='Cuando hayas completado los pasos anteriores presiona el botón `✅Completado`. Cuando lo presiones nos confirmas que estas de acuerdo con las Advertencias.', inline=False)
            embed_reportes.add_field(name='Advertencias', value='**1.** No aceptamos reportes sobre problemas personales.\n**2.** No aceptamos reportes si no escribes la ID del usuario', inline=False)
            embed_reportes.set_image(url='https://i.imgur.com/MbrEHnw.jpg')
            await canal.send(interaction.author.mention, embed=embed_reportes, components = [[
                Button(custom_id = 'llamar_staff', label = "Completado", style = ButtonStyle.green, emoji='✅'),
                Button(custom_id = 'cerrar_ticket', label = "Cerrar ticket", style = ButtonStyle.red,emoji ='🔐')]])


        if interaction.values[0] == 'regalar':
            canal = await guild.create_text_channel(name=f'🎁┃{interaction.author.name}-ticket', category=category)
            await canal.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await canal.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)
            await canal.set_permissions(rol_staff,
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True,
                                                manage_messages=True)

            await interaction.send(f'> Se creó el canal {canal.mention} para que hagas tus regalos 🎁')

            embed_regalar = discord.Embed(title=f'Regalos - ¡Hola {interaction.author.name}!', description='¿Quieres obsequiar algo?, sigue estos pasos:', color=embed_color)
            embed_regalar.add_field(name='Paso 1', value='Leer las advertencias.', inline=False)
            embed_regalar.add_field(name='Paso 2', value='Escribenos que es lo que quieres obsequiar.', inline=False)
            embed_regalar.add_field(name='Paso 3', value='Cuando hayas completado los pasos anteriores presiona el botón `✅Completado`. Cuando lo presiones nos confirmas que estas de acuerdo con las Advertencias.', inline=False)
            embed_regalar.add_field(name='Advertencias', value='**1.** No aceptamos cuentas crackeadas, bineadas, ni temas sobre carding.\n**2.** Cuando te comprometas con un sorteo debes cumplirlo o recibirás una sanción.\n**3.** No aceptamos información personal, datos bancarios, ni acceder a cuentas.', inline=False)
            await canal.send(interaction.author.mention, embed=embed_regalar, components = [[
                Button(custom_id = 'llamar_staff', label = "Completado", style = ButtonStyle.green, emoji='✅'),
                Button(custom_id = 'cerrar_ticket', label = "Cerrar ticket", style = ButtonStyle.red,emoji ='🔐')]])

        if interaction.values[0] == 'patrocinador':
            canal = await guild.create_text_channel(name=f'🛒┃{interaction.author.name}-ticket', category=category)
            await canal.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await canal.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)
            await canal.set_permissions(rol_staff,
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True,
                                                manage_messages=True)

            await interaction.send(f'> Se creó el canal {canal.mention} para que hagas tu compra 🛒')

            embed_patrocinador = discord.Embed(title=f'Comprar Patrocinador - ¡Hola {interaction.author.name}!', description='En este ticket podrás comprar el rol <@&764318598230573056>',color=embed_color)
            embed_patrocinador.add_field(name='¿Qué beneficios trae?', value='Mira los beneficios en <#845508811699912704>', inline=False)
            embed_patrocinador.add_field(name='¿Cuanto cuesta el rol?', value='El rol tiene un costo de `$5.000 COP`', inline=False)
            embed_patrocinador.add_field(name='¿Qué metodos de pago hay?', value='> Nequi: `3108188596`\n> Paypal: `beerfx357@gmail.com`\n> Patreon: [Click aquí](https://www.patreon.com/lospibardos)',inline=False )
            embed_patrocinador.set_image(url='https://i.imgur.com/U224JqE.jpg')
            await canal.send(interaction.author.mention, embed=embed_patrocinador,components = [[
                    Button(
                        custom_id = 'ya_pague',
                        label = "Ya realicé el pago",
                        style = ButtonStyle.green,
                        emoji ='✅'),
                    Button(
                        custom_id = 'llamar_staff',
                        label = "Necesito ayuda",
                        style = ButtonStyle.blue,
                        emoji ='🔔')],[
                    Button(
                        custom_id = 'cerrar_ticket',
                        label = "Cerrar ticket",
                        style = ButtonStyle.red,
                        emoji ='🔐')]])

        if interaction.values[0] == 'desbaneos':
            canal = await guild.create_text_channel(name=f'📄┃{interaction.author.name}-ticket', category=category)
            await canal.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await canal.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)
            await canal.set_permissions(rol_staff,
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True,
                                                manage_messages=True)

            await interaction.send(f'> Se creó el canal {canal.mention} para saber como ser desbaneado 📄')

            embed_desbaneos = discord.Embed(title=f'Desbaneos - ¡Hola {interaction.author.name}!', description='¿Quieres saber como ser desbaneado?\n\nPara ser desbaneado deberas entrar al siguiente servidor y abrir un ticket en el canal de <#890052840855314452>\n\nTambien puedes compartir el servidor con un amigo o persona que conozcas que esté baneado del servidor principal.', color=embed_color)
            embed_desbaneos.set_image(url='https://i.imgur.com/6KBhYGt.jpg')
            await canal.send(f'{interaction.author.mention} https://discord.gg/q2vuK4aHYM', embed=embed_desbaneos, components = [[
                Button(custom_id = 'llamar_staff', label = "Necesito ayuda", style = ButtonStyle.blue, emoji='🔔'),
                Button(custom_id = 'cerrar_ticket', label = "Cerrar ticket", style = ButtonStyle.red,emoji ='🔐')]])

@bot.command(aliases=['help'])
@commands.cooldown(1, 3, commands.BucketType.user)
async def ayuda(ctx):
    embed = discord.Embed(title='Comandos de Pibarbot', description='> **Prefix:** `pb!`', color=embed_color)
    embed.add_field(name="» Diversión", value='```pregunta          pipi            dado             gay```', inline= False)
    embed.add_field(name="» Reacción", value='```abrazar           besar           pensar           golpear\nnalguear          llorar          bailar           enojado\ndormir            vomitar         comer            asustado\ndisparar          saludar         lamer            aplaudir```', inline= False)
    embed.add_field(name="» Útilidad", value='```servidor          banner          icono            avatar```', inline= False)
    embed.set_footer(text="© Pibarbot 2021")
    await ctx.reply(embed = embed, components = [
            Button(
                custom_id = 'apoyar_pibarbot',
                label = "Apoyar Pibarbot",
                style = ButtonStyle.green,
                url = 'https://discord.com/channels/745672936131657768/882251364288319509/882252645417488425',
                emoji ='⭐')])
           
           
bot.run('')