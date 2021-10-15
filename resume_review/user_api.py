import logging

from resume_review.models import Account, Reviewer, Comment

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


def get_good_reviewer():
    good_reviewer = []
    reviewers = Reviewer.objects.all()
    for r in reviewers:
        comments = Comment.objects.filter(reviewer=r)
        rate_sum = 0
        for c in comments:
            rate_sum += c.rate
        ave_rate = rate_sum / comments.len()
        if ave_rate > 4.5:
            good_reviewer.append(r)
        return good_reviewer
