import logging

from resume_review.models import Account, Reviewer, Comment, Order

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
        orders = Order.objects.filter(order_id=order_id)
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
        comments = Comment.objects.filter(reviewer=r)
        rate_sum = 0
        for c in comments:
            rate_sum += c.rate

        ave_rate = rate_sum / len(comments) if len(comments) != 0 else 0

        if ave_rate > 4.5:
            good_reviewer.append(r)
        return good_reviewer
