import logging

from resume_review.models import Account, Reviewer, Comment, Order, Room
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


def is_reviewer(user):
    '''
    check whether a user is a reviewer
    :param user: User object
    :return: True/False
    '''
    try:
        accounts = Account.objects.filter(user=user)
        if len(accounts) == 0:
            logger.error('cannot find account for user %s' % user)
            return False

        account = accounts[0]
        reviewers = Reviewer.objects.filter(account=account)
        return len(reviewers) != 0
    except:
        logger.error('is_reviewer failed')
    return False


def get_reviewer_by_account(account):
    '''
    get the reviewer obj by account
    :param account:  Account Obj
    :return: Reviewer Obj
    '''
    try:
        reviewers = Reviewer.objects.filter(account=account)
        if len(reviewers) == 0:
            logger.error('cannot find reviewer for %s' % account.user)
            return None
        return reviewers[0]
    except:
        logger.error('get_reviewer_by_account failed')
    return None


def get_account_by_user(user):
    '''
    get the account object by user
    :param user: user object
    :return:
    '''
    try:
        accounts = Account.objects.filter(user=user)
        if len(accounts) == 0:
            logger.error('cannot find account for user %s' % user)
            return None
        return accounts[0]
    except:
        logger.error('get_account_by_user failed')
    return None


def get_order(order_id):
    '''
    get the order object by order id
    :param order_id:
    :return: order obj
    '''
    try:
        orders = Order.objects.filter(id=order_id)
        if len(orders) == 0:
            logger.error('cannot find order for %s' % order_id)
            return None
        return orders[0]
    except:
        logger.error('get_order failed')
    return None


def get_good_reviewer():
    '''
    get the reviewer with rates > 4.5
    :return: a list of good reviewer
    '''
    good_reviewer = []
    reviewers = Reviewer.objects.all()
    for r in reviewers:
        rate = get_average_rating(r)
        r.rate = rate
        r.save()

        if rate >= 4.0:
            good_reviewer.append(r)
    return good_reviewer


def create_test_database():
    # user = User.objects.create_user(username='user1', email='user1@case.edu', password="111111")
    # account1 = Account.objects.create(user=user)
    #
    # user = User.objects.get(username='user1')
    # account1 = Account.objects.get(user=user)
    #
    #
    # user = User.objects.get(username='user2')
    # account2 = Account.objects.get(user=user)
    # reviewer2 = Reviewer.objects.get(account=account2)
    #
    # user = User.objects.get(username='user3')
    # account3 = Account.objects.get(user=user)
    # reviewer3 = Reviewer.objects.get(account=account3)
    #
    # user = User.objects.get(username='user4')
    # account4 = Account.objects.get(user=user)
    # reviewer4 = Reviewer.objects.get(account=account2)

    reviewers = Reviewer.objects.all()
    for reviewer in reviewers:
        reviewer.delivery_time = 'One week'
        reviewer.save()

    # Order.objects.create(account=account2, reviewer=reviewer4, state='Rejected')

    # user = User.objects.create_user(username='user3', email='user3@case.edu', password="111111")
    # account3 = Account.objects.create(user=user)
    # reviewer3 = Reviewer.objects.create(account=account3)
    #
    # user = User.objects.create_user(username='user4', email='user4@case.edu', password="111111")
    # account4 = Account.objects.create(user=user)
    # reviewer4 = Reviewer.objects.create(account=account4)

    # Order.objects.create(account=account1, reviewer=reviewer2)
    # Order.objects.create(account=account1, reviewer=reviewer3)
    # Order.objects.create(account=account1, reviewer=reviewer3)
    # Order.objects.create(account=account2, reviewer=reviewer3)
    # Order.objects.create(account=account2, reviewer=reviewer4)
    # Order.objects.create(account=account4, reviewer=reviewer2)


def get_average_rating(r):
    comments = Comment.objects.filter(reviewer=r)
    rate_sum = 0
    for comment in comments:
        rate_sum += float(comment.rate)

    if len(comments) == 0:
        average_rate = 0
    else:
        average_rate = rate_sum/len(comments)
    return round(average_rate, 2)



def get_room_info(account):
    '''
    get a dict list of all chat room info
    :param account: Account obj
    :return: a dict list of room info
    '''
    res = []
    try:
        ## as user
        rooms = Room.objects.filter(account=account)
        for room in rooms:
            room_info = {}
            room_info['room'] = room
            room_info['current_user'] = account
            room_info['other_user'] = room.reviewer.account
            res.append(room_info)

        ## as reviewer
        reviewer = get_reviewer_by_account(account)
        if reviewer:
            rooms = Room.objects.filter(reviewer=reviewer)
            for room in rooms:
                room_info = {}
                room_info['room'] = room
                room_info['current_user'] = reviewer
                room_info['other_user'] = room.account
                res.append(room_info)
    except:
        logger.error('get_room_info failed')
    return res


def get_contactor_by_room(account, current_room):
    '''
    get the contactor by the current user and room
    :param account: Account obj
    :param current_room: Room obj
    :return: the Account obj of the other user
    '''
    rooms = get_room_info(account)
    for room in rooms:
        if room['current_user'] == account and room['room'] == current_room:
            return room['other_user']
    return None


def generate_msg_dict(message):
    '''
    generate a dict for msg information
    :param message: Message obj
    :return: a dict of message info
    '''
    res = {}
    res['value'] = message.value
    res['account_id'] = message.account.id
    res['account_name'] = message.account.first_name + ' ' + message.account.last_name
    res['avatar_url'] = message.account.avatar.url
    res['date'] = message.date.strftime("%m/%d/%Y, %H:%M:%S")

    return res
