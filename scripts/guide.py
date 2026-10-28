"""实用分级页的数据：主榜 + 升星榜头部，按实用性分档（档位定义在 config.yml 的 guide.tiers），每个写几条应用场景。

升星榜头部 = 升星榜里写一句话介绍、但不在主榜的项目，多是创建超过 90 天、主榜收不到的老项目。
guide.surge_full_intro 打开时，给它们也读完整 README 写介绍：和主榜共用 data/intros/ 缓存，
之后进了主榜直接复用，README 没变也不会重写。分级只读介绍，不再读 README。
"""
import fetch


def surge_heads(rising_data):
    if not rising_data:
        return []
    return [x for x in rising_data["surge"] if x["featured"] and not x["in_main"]]


def _surge_entries(cfg, today, summ, heads, flags_of):
    """补齐元数据和 README（升星榜只存了精简字段），生成完整介绍。单个失败跳过，不影响其他项目。"""
    s = fetch._session()
    out = []
    for x in heads:
        try:
            r = fetch._get(s, f"{fetch.API}/repos/{x['full_name']}")
            if r.status_code != 200:
                raise RuntimeError(f"HTTP {r.status_code}")
            repo = fetch.add_readme(s, fetch._slim(r.json()), cfg["readme_max_chars"])
        except Exception as e:  # 网络抖动等，只影响这一个
            print(f"  ! {x['full_name']} 元数据或 README 获取失败，不进分级页：{type(e).__name__}: {e}")
            continue
        intro = summ.intro(repo, today)  # AuthError 照常上抛，整期中止
        repo.pop("readme", None)
        if not intro["is_ai_product"]:
            continue
        out.append({**repo, "intro": intro, "flags": flags_of(repo),
                    **{k: x[k] for k in ("last7", "prev7", "accel")}})
    return out


def build(cfg, today, entries, rising_data, summ, flags_of):
    """返回写进快照的 guide 字段：升星榜头部的完整条目、每个项目的分级、疑似刷星名单。"""
    g = cfg["guide"]
    surge = _surge_entries(cfg, today, summ, surge_heads(rising_data), flags_of) if g.get("surge_full_intro") else []
    suspects = {x["full_name"] for x in rising_data["suspects"]} if rising_data else set()
    items = [{"full_name": e["full_name"], "stars": e["stars"], "intro": e["intro"], "flags": e["flags"],
              "suspect": e["full_name"] in suspects} for e in entries + surge]
    practical = summ.practical(items)
    print(f"   分级 {len(practical)}/{len(items)} 个（主榜 {len(entries)}，升星榜头部 {len(surge)}）")
    return {"surge": surge, "practical": practical, "suspects": sorted(suspects & set(practical))}
