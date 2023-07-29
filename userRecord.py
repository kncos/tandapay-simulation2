from enum import Enum
from typing import List

class ValidityEnum(Enum):
    VALID = 0
    INVALID = 1
    NR = 2


class PrimaryRoleEnum(Enum):
    DEFECTOR = 0
    LOW_MORALE = 1
    UNITY = 2


class SecondaryRoleEnum(Enum):
    DEPENDENT = 0
    INDEPENDENT = 1


class CurrentStatusEnum(Enum):
    PAID = 0
    DEFECTED = 1
    SKIPPED = 2
    PAID_INVALID = 3
    QUIT = 4
    REORG = 5
    NR = 6


class PayableEnum(Enum):
    YES = 0
    NO = 1
    NR = 2


class UserRecord:
    def __init__(self, count: int, bundling: int):
        self._orig_sbg_num = 0                              # UsRec1: Original assigned subgroup number (generated by subgroup setup)
        self._remaining_orig_sbg = 0                        # UsRec2: Number of members remaining from original subgroup (generated by subgroup setup)
        self._cur_sbg_num = 0                               # UsRec3: Current assigned subgroup number (generated by subgroup setup)
        self._members_cur_sbg = 0                           # UsRec4: Number of members in current subgroup (generated by subgroup setup)
        self._sbg_status = ValidityEnum.VALID               # UsRec5: Status of subgroup Accepted values: Valid, Invalid, or NR (initialize to VALID)
        self._pri_role = PrimaryRoleEnum.DEFECTOR           # UsRec6: Primary role. Accepted values: Defector, Low-Morale, or Unity (generated by the role-assignment)
        self._sec_role = SecondaryRoleEnum.DEPENDENT        # UsRec7: Secondary role. Accepted values: Dependent or independent (generated by the role-assignment)
        self._cur_status = CurrentStatusEnum.PAID           # UsRec8: Current status, Accepted values: Defected, Paid, Skipped, Paid-Invalid, Quit, Reorg, or NR (initialize to PAID)
        self._reorged_cnt = 0                               # UsRec9: Number of times they have reorged (initialize to 0)
        self._payable = PayableEnum.YES                     # UsRec12: A member's ability to pay this periodAccepted values: Yes, No, or NR (initialize to YES)
        self._defector_cnt = 0                              # UsRec13: Defector counter
        self._wallet_balance = 0                            # User's wallet balance
        self._wallet_claim_award = 0                        # TODO: No description provided
        self._wallet_no_claim_refund = 0                    # No claim in the previous month refund (?)
        self._wallet_reorg_refund = 0                       # Reorganiztion from previous month refund. This refund is awarded to the user if they were reorged in the previous month.
        self._cur_month_first_calc = 0                      # Current month's first premium calculation
        self._cur_month_balance = 0                         # Current month's balance
        self._cur_month_premium = 0                         # Current month's premium
        self._cur_month_second_calc_list = [0] * count      # cur_month_second_calc_list[i] = Current month's second premium calculation from (i+1) period
        self._prior_month_premium_list = [0] * bundling     # prior_month_premium_list[i] = premium from i+1 months ago
        self._total_value_refund_list = [0] * count         # total value of the refund from period (i+1)
        self._debit_to_savings_account_list = [0] * count   # amount debited to savings account in period (i+1)                                                                      

# TODO: Add logic as needed for interacting with lists, avoid hacky encapsulation-breaking fixes.

# Getters with bounds checking for the lists
    def get_current_month_second_premium_calculation(self, period):
        if (0 < period <= len(self._cur_month_second_calc_list)):
            return self._cur_month_second_calc_list[period-1]
        else:
            raise IndexError("Attempting to access out of bounds index for cur_month_second_calc_list.")
    
    def get_prior_month_premium(self, num_months_ago):
        if(0 < num_months_ago <= len(self._prior_month_premium_list)):
            return self._prior_month_premium_list[num_months_ago - 1]
        else:    
            raise IndexError("Attempting to access out of bounds index for prior_month_premium_list")
         
    def get_total_refund_value(self, period):
        if(0 < period <= len(self._total_value_refund_list)):
            return self._total_value_refund_list[period - 1]
        else:
            raise IndexError("Attempting to access out of bounds index for total_value_refund_list")

    def get_debit_to_savings_account(self, period):
        if(0 < period <= len(self._debit_to_savings_account_list)):
            return self._debit_to_savings_account_list[period - 1]
        else:
            raise IndexError("Attempting to access out of bounds index for debit_to_savings_account_list")

# UsRec1: Original assigned subgroup number
    @property
    def orig_sbg_num(self):
        return self._orig_sbg_num

    @orig_sbg_num.setter
    def orig_sbg_num(self, value):
        self._orig_sbg_num = value

# UsRec2: Number of members remaining from original subgroup
    @property
    def remaining_orig_sbg(self):
        return self._remaining_orig_sbg

    @remaining_orig_sbg.setter
    def remaining_orig_sbg(self, value):
        self._remaining_orig_sbg = value

# UsRec3: Current assigned subgroup number
    @property
    def cur_sbg_num(self):
        return self._cur_sbg_num

    @cur_sbg_num.setter
    def cur_sbg_num(self, value):
        self._cur_sbg_num = value

# UsRec4: Number of members in current subgroup
    @property
    def members_cur_sbg(self):
        return self._members_cur_sbg

    @members_cur_sbg.setter
    def members_cur_sbg(self, value):
        self._members_cur_sbg = value

# UsRec5: Status of subgroup
    @property
    def sbg_status(self):
        return self._sbg_status

    @sbg_status.setter
    def sbg_status(self, value):
        self._sbg_status = value

# UsRec6: Primary role
    @property
    def pri_role(self):
        return self._pri_role

    @pri_role.setter
    def pri_role(self, value):
        self._pri_role = value

# UsRec7: Secondary role
    @property
    def sec_role(self):
        return self._sec_role

    @sec_role.setter
    def sec_role(self, value):
        self._sec_role = value

# UsRec8: Current status
    @property
    def cur_status(self):
        return self._cur_status

    @cur_status.setter
    def cur_status(self, value):
        self._cur_status = value

# UsRec9: Number of times they have reorged
    @property
    def reorged_cnt(self):
        return self._reorged_cnt

    @reorged_cnt.setter
    def reorged_cnt(self, value):
        self._reorged_cnt = value

# UsRec12: A member's ability to pay this period
    @property
    def payable(self):
        return self._payable

    @payable.setter
    def payable(self, value):
        self._payable = value

# UsRec13: Defector counter
    @property
    def defector_cnt(self):
        return self._defector_cnt

    @defector_cnt.setter
    def defector_cnt(self, value):
        self._defector_cnt = value

# User's wallet balance
    @property
    def wallet_balance(self):
        return self._wallet_balance

    @wallet_balance.setter
    def wallet_balance(self, value):
        self._wallet_balance = value

# TODO: No description provided
    @property
    def wallet_claim_award(self):
        return self._wallet_claim_award

    @wallet_claim_award.setter
    def wallet_claim_award(self, value):
        self._wallet_claim_award = value

# No claim in the previous month refund
    @property
    def wallet_no_claim_refund(self):
        return self._wallet_no_claim_refund

    @wallet_no_claim_refund.setter
    def wallet_no_claim_refund(self, value):
        self._wallet_no_claim_refund = value

# Reorganiztion from previous month refund
    @property
    def wallet_reorg_refund(self):
        return self._wallet_reorg_refund

    @wallet_reorg_refund.setter
    def wallet_reorg_refund(self, value):
        self._wallet_reorg_refund = value

# Current month's first premium calculation
    @property
    def cur_month_first_calc(self):
        return self._cur_month_first_calc

    @cur_month_first_calc.setter
    def cur_month_first_calc(self, value):
        self._cur_month_first_calc = value

# Current month's balance
    @property
    def cur_month_balance(self):
        return self._cur_month_balance

    @cur_month_balance.setter
    def cur_month_balance(self, value):
        self._cur_month_balance = value

# Current month's premium
    @property
    def cur_month_premium(self):
        return self._cur_month_premium

    @cur_month_premium.setter
    def cur_month_premium(self, value):
        self._cur_month_premium = value

