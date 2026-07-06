from app.matcher.preferences.base import BasePreference

COMPANIES = {
    "Datadog": 20,
    "Cloudflare": 20,
    "Stripe": 15,
    "MongoDB": 15,
}


class CompanyPreference(BasePreference):

    def apply(self, job, result):

        weight = COMPANIES.get(job.company)

        if weight:

            result.add(
                type="company",
                value=job.company,
                weight=weight,
            )