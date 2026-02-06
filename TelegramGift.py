from telethon import TelegramClient, functions, types

api_id = 123456      # your api_id
api_hash = "YOUR_API_HASH"  # your api_hash
session = "star_gift_cli"

client = TelegramClient(session, api_id, api_hash)


async def main():
    gift_id_str = input("Enter gift id: ").strip()
    user_id_str = input("Enter user id: ").strip()
    comment = input("Enter comment (optional): ").strip()

    if not gift_id_str or not user_id_str:
        print("gift id and user id are required")
        return

    try:
        gift_id = int(gift_id_str)
        user_id = int(user_id_str)
    except ValueError:
        print("gift id and user id must be integers")
        return

    full = await client(functions.users.GetFullUserRequest(user_id))
    user = full.users[0]
    ip_peer = types.InputPeerUser(user_id=user.id, access_hash=user.access_hash)

    if comment:
        msg_with_entities = types.TextWithEntities(
            text=comment,
            entities=[]
        )
    else:
        msg_with_entities = None

    invoice = types.InputInvoiceStarGift(
        peer=ip_peer,
        gift_id=gift_id,
        hide_name=False,
        include_upgrade=False,
        message=msg_with_entities
    )

    payment_form = await client(functions.payments.GetPaymentFormRequest(
        invoice=invoice
    ))

    result = await client(functions.payments.SendStarsFormRequest(
        form_id=payment_form.form_id,
        invoice=invoice
    ))

    print("Done:", result)


with client:
    client.loop.run_until_complete(main())
