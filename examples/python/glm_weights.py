#!/usr/bin/env python

# DO NOT EDIT
# Autogenerated from the notebook glm_weights.ipynb.
# Edit the notebook and then sync the output with this file.
#
# flake8: noqa
# DO NOT EDIT

# # Weighted Generalized Linear Models

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm

# ## Weighted GLM: Poisson response data
#
# ### Load data
#
# In this example, we'll use the affair dataset using a handful of
# exogenous variables to predict the extra-marital affair rate.
#
# Weights will be generated to show that `freq_weights` are equivalent to
# repeating records of data. On the other hand, `var_weights` is equivalent
# to aggregating data.

print(sm.datasets.fair.NOTE)

# Load the data into a pandas dataframe.

data = sm.datasets.fair.load_pandas().data

#  The dependent (endogenous) variable is ``affairs``

data.describe()

data[:3]

# In the following we will work mostly with Poisson. While using decimal
# affairs works, we convert them to integers to have a count distribution.

data["affairs"] = np.ceil(data["affairs"])
data[:3]

(data["affairs"] == 0).mean()

np.bincount(data["affairs"].astype(int))

# ## Condensing and Aggregating observations
#
# We have 6366 observations in our original dataset. When we consider only
# some selected variables, then we have fewer unique observations. In the
# following we combine observations in two ways, first we combine
# observations that have values for all variables identical, and secondly we
# combine observations that have the same explanatory variables.

# ### Dataset with unique observations
#
# We use pandas's groupby to combine identical observations and create a
# new variable `freq` that count how many observation have the values in the
# corresponding row.

data2 = data.copy()
data2["const"] = 1
dc = (data2["affairs rate_marriage age yrs_married const".split()].groupby(
    "affairs rate_marriage age yrs_married".split()).count())
dc.reset_index(inplace=True)
dc.rename(columns={"const": "freq"}, inplace=True)
print(dc.shape)
dc.head()

# ### Dataset with unique explanatory variables (exog)
#
# For the next dataset we combine observations that have the same values
# of the explanatory variables. However, because the response variable can
# differ among combined observations, we compute the mean and the sum of the
# response variable for all combined observations.
#
# We use again pandas ``groupby`` to combine observations and to create
# the new variables. We also flatten the ``MultiIndex`` into a simple index.

gr = data["affairs rate_marriage age yrs_married".split()].groupby(
    "rate_marriage age yrs_married".split())
df_a = gr.agg(["mean", "sum", "count"])


def merge_tuple(tpl):
    if isinstance(tpl, tuple) and len(tpl) > 1:
        return "_".join(map(str, tpl))
    else:
        return tpl


df_a.columns = df_a.columns.map(merge_tuple)
df_a.reset_index(inplace=True)
print(df_a.shape)
df_a.head()

# After combining observations with have a dataframe `dc` with 467 unique
# observations, and a dataframe `df_a` with 130 observations with unique
# values of the explanatory variables.

print("number of rows: \noriginal, with unique observations, with unique exog")
data.shape[0], dc.shape[0], df_a.shape[0]

# ## Analysis
#
# In the following, we compare the GLM-Poisson results of the original
# data with models of the combined observations where the multiplicity or
# aggregation is given by weights or exposure.
#
#
# ### original data

glm = smf.glm(
    "affairs ~ rate_marriage + age + yrs_married",
    data=data,
    family=sm.families.Poisson(),
)
res_o = glm.fit()
print(res_o.summary())

res_o.pearson_chi2 / res_o.df_resid

# ### condensed data (unique observations with frequencies)
#
# Combining identical observations and using frequency weights to take
# into account the multiplicity of observations produces exactly the same
# results. Some results attribute will differ when we want to have
# information about the observation and not about the aggregate of all
# identical observations. For example, residuals do not take
# ``freq_weights`` into account.

glm = smf.glm(
    "affairs ~ rate_marriage + age + yrs_married",
    data=dc,
    family=sm.families.Poisson(),
    freq_weights=np.asarray(dc["freq"]),
)
res_f = glm.fit()
print(res_f.summary())

res_f.pearson_chi2 / res_f.df_resid

# ### condensed using ``var_weights`` instead of ``freq_weights``
#
# Next, we compare ``var_weights`` to ``freq_weights``. It is a common
# practice to incorporate ``var_weights`` when the endogenous variable
# reflects averages and not identical observations.
# I do not see a theoretical reason why it produces the same results (in
# general).
#
# This produces the same results but ``df_resid``  differs the
# ``freq_weights`` example because ``var_weights`` do not change the number
# of effective observations.
#

glm = smf.glm(
    "affairs ~ rate_marriage + age + yrs_married",
    data=dc,
    family=sm.families.Poisson(),
    var_weights=np.asarray(dc["freq"]),
)
res_fv = glm.fit()
print(res_fv.summary())

# Dispersion computed from the results is incorrect because of wrong
# ``df_resid``.
# It is correct if we use the original ``df_resid``.

res_fv.pearson_chi2 / res_fv.df_resid, res_f.pearson_chi2 / res_f.df_resid

# ### aggregated or averaged data (unique values of explanatory variables)
#
# For these cases we combine observations that have the same values of the
# explanatory variables. The corresponding response variable is either a sum
# or an average.
#
# #### using ``exposure``
#
# If our dependent variable is the sum of the responses of all combined
# observations, then under the Poisson assumption the distribution remains
# the same but we have varying `exposure` given by the number of individuals
# that are represented by one aggregated observation.
#
# The parameter estimates and covariance of parameters are the same with
# the original data, but log-likelihood, deviance and Pearson chi-squared
# differ

glm = smf.glm(
    "affairs_sum ~ rate_marriage + age + yrs_married",
    data=df_a,
    family=sm.families.Poisson(),
    exposure=np.asarray(df_a["affairs_count"]),
)
res_e = glm.fit()
print(res_e.summary())

res_e.pearson_chi2 / res_e.df_resid

# #### using var_weights
#
# We can also use the mean of all combined values of the dependent
# variable. In this case the variance will be related to the inverse of the
# total exposure reflected by one combined observation.

glm = smf.glm(
    "affairs_mean ~ rate_marriage + age + yrs_married",
    data=df_a,
    family=sm.families.Poisson(),
    var_weights=np.asarray(df_a["affairs_count"]),
)
res_a = glm.fit()
print(res_a.summary())

# ### Comparison
#
# We saw in the summary prints above that ``params`` and ``cov_params``
# with associated Wald inference agree across versions. We summarize this in
# the following comparing individual results attributes across versions.
#
# Parameter estimates `params`, standard errors of the parameters `bse`
# and `pvalues` of the parameters for the tests that the parameters are
# zeros all agree. However, the likelihood and goodness-of-fit statistics,
# `llf`, `deviance` and `pearson_chi2` only partially agree. Specifically,
# the aggregated version do not agree with the results using the original
# data.
#
# **Warning**: The behavior of `llf`, `deviance` and `pearson_chi2` might
# still change in future versions.
#
# Both the sum and average of the response variable for unique values of
# the explanatory variables have a proper likelihood interpretation.
# However, this interpretation is not reflected in these three statistics.
# Computationally this might be due to missing adjustments when aggregated
# data is used. However, theoretically we can think in these cases,
# especially for `var_weights` of the misspecified case when likelihood
# analysis is inappropriate and the results should be interpreted as quasi-
# likelihood estimates. There is an ambiguity in the definition of
# ``var_weights`` because they can be used for averages with correctly
# specified likelihood as well as for variance adjustments in the quasi-
# likelihood case. We are currently not trying to match the likelihood
# specification. However, in the next section we show that likelihood ratio
# type tests still produce the same result for all aggregation versions when
# we assume that the underlying model is correctly specified.

results_all = [res_o, res_f, res_e, res_a]
names = "res_o res_f res_e res_a".split()

pd.concat([r.params for r in results_all], axis=1, keys=names)

pd.concat([r.bse for r in results_all], axis=1, keys=names)

pd.concat([r.pvalues for r in results_all], axis=1, keys=names)

pd.DataFrame(
    np.column_stack([[r.llf, r.deviance, r.pearson_chi2]
                     for r in results_all]),
    columns=names,
    index=["llf", "deviance", "pearson chi2"],
)

# ### Likelihood Ratio type tests
#
# We saw above that likelihood and related statistics do not agree between
# the aggregated and original, individual data. We illustrate in the
# following that likelihood ratio test and difference in deviance agree
# across versions, however Pearson chi-squared does not.
#
# As before: This is not sufficiently clear yet and could change.
#
# As a test case we drop the `age` variable and compute the likelihood
# ratio type statistics as difference between reduced or constrained and
# full or unconstrained model.

# #### original observations and frequency weights

glm = smf.glm("affairs ~ rate_marriage + yrs_married",
              data=data,
              family=sm.families.Poisson())
res_o2 = glm.fit()
# print(res_f2.summary())
res_o2.pearson_chi2 - res_o.pearson_chi2, res_o2.deviance - res_o.deviance, res_o2.llf - res_o.llf

glm = smf.glm(
    "affairs ~ rate_marriage + yrs_married",
    data=dc,
    family=sm.families.Poisson(),
    freq_weights=np.asarray(dc["freq"]),
)
res_f2 = glm.fit()
# print(res_f2.summary())
res_f2.pearson_chi2 - res_f.pearson_chi2, res_f2.deviance - res_f.deviance, res_f2.llf - res_f.llf

# #### aggregated data: ``exposure`` and ``var_weights``
#
# Note: LR test agrees with original observations, ``pearson_chi2``
# differs and has the wrong sign.

glm = smf.glm(
    "affairs_sum ~ rate_marriage + yrs_married",
    data=df_a,
    family=sm.families.Poisson(),
    exposure=np.asarray(df_a["affairs_count"]),
)
res_e2 = glm.fit()
res_e2.pearson_chi2 - res_e.pearson_chi2, res_e2.deviance - res_e.deviance, res_e2.llf - res_e.llf

glm = smf.glm(
    "affairs_mean ~ rate_marriage + yrs_married",
    data=df_a,
    family=sm.families.Poisson(),
    var_weights=np.asarray(df_a["affairs_count"]),
)
res_a2 = glm.fit()
res_a2.pearson_chi2 - res_a.pearson_chi2, res_a2.deviance - res_a.deviance, res_a2.llf - res_a.llf

# ### Investigating Pearson chi-square statistic
#
# First, we do some sanity checks that there are no basic bugs in the
# computation of `pearson_chi2` and `resid_pearson`.

res_e2.pearson_chi2, res_e.pearson_chi2, (res_e2.resid_pearson**2).sum(), (
    res_e.resid_pearson**2).sum()

res_e._results.resid_response.mean(), res_e.model.family.variance(
    res_e.mu)[:5], res_e.mu[:5]

(res_e._results.resid_response**2 /
 res_e.model.family.variance(res_e.mu)).sum()

res_e2._results.resid_response.mean(), res_e2.model.family.variance(
    res_e2.mu)[:5], res_e2.mu[:5]

(res_e2._results.resid_response**2 /
 res_e2.model.family.variance(res_e2.mu)).sum()

(res_e2._results.resid_response**2).sum(), (
    res_e._results.resid_response**2).sum()

# One possible reason for the incorrect sign is that we are subtracting
# quadratic terms that are divided by different denominators. In some
# related cases, the recommendation in the literature is to use a common
# denominator. We can compare pearson chi-squared statistic using the same
# variance assumption in the full and reduced model.
#
# In this case we obtain the same pearson chi2 scaled difference between
# reduced and full model across all versions. (Issue
# [#3616](https://github.com/statsmodels/statsmodels/issues/3616) is
# intended to track this further.)

((res_e2._results.resid_response**2 - res_e._results.resid_response**2) /
 res_e2.model.family.variance(res_e2.mu)).sum()

((res_a2._results.resid_response**2 - res_a._results.resid_response**2) /
 res_a2.model.family.variance(res_a2.mu) * res_a2.model.var_weights).sum()

((res_f2._results.resid_response**2 - res_f._results.resid_response**2) /
 res_f2.model.family.variance(res_f2.mu) * res_f2.model.freq_weights).sum()

((res_o2._results.resid_response**2 - res_o._results.resid_response**2) /
 res_o2.model.family.variance(res_o2.mu)).sum()

# ## Remainder
#
# The remainder of the notebook just contains some additional checks and
# can be ignored.

np.exp(res_e2.model.exposure)[:5], np.asarray(df_a["affairs_count"])[:5]

res_e2.resid_pearson.sum() - res_e.resid_pearson.sum()

res_e2.mu[:5]

res_a2.pearson_chi2, res_a.pearson_chi2, res_a2.resid_pearson.sum(
), res_a.resid_pearson.sum()

((res_a2._results.resid_response**2) /
 res_a2.model.family.variance(res_a2.mu) * res_a2.model.var_weights).sum()

((res_a._results.resid_response**2) / res_a.model.family.variance(res_a.mu) *
 res_a.model.var_weights).sum()

((res_a._results.resid_response**2) / res_a.model.family.variance(res_a2.mu) *
 res_a.model.var_weights).sum()

res_e.model.endog[:5], res_e2.model.endog[:5]

res_a.model.endog[:5], res_a2.model.endog[:5]

res_a2.model.endog[:5] * np.exp(res_e2.model.exposure)[:5]

res_a2.model.endog[:5] * res_a2.model.var_weights[:5]

from scipy import stats

stats.chi2.sf(27.19530754604785, 1), stats.chi2.sf(29.083798806764687, 1)

res_o.pvalues

print(res_e2.summary())
print(res_e.summary())

print(res_f2.summary())
print(res_f.summary())
