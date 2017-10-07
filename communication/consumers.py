# import json
# from channels import Group
# from channels.sessions import channel_session
# from urllib.parse import parse_qs

#
# @channel_session
# def ws_connect(message, room_name):
#     message.reply_channel.send({'accept': True})
#     params = parse_qs(message.context['query_string'])
#
#     if b'username' in params:
#         message.channel_session['username'] = params[b'username'][0].decode('utf8')
#         Group('chat-%s' % room_name).add(message.reply_channel)
#     else:
#         message.reply_channel.send({'close': True})
#
#
# @channel_session
# def ws_message(message, room_name):
#     Group('chat-%s' % room_name).send({
#         'text': json.dumps({
#             'text': message['text'],
#             'username': message.channel_session['username'],
#         }),
#     })
#
#
# def ws_disconnect(message, room_name):
#     Group('chat-%s' % room_name).discard(message.reply_channel)
